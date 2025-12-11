package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"

	"github.com/draffensperger/golp"
)

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each machine
	total := 0
	for scanner.Scan() {
		// Parse line to get lights and buttons information
		final_state, actions := parse_part1(scanner.Text())

		// Run BFS from start state to final state
		total += bfs1(final_state, actions)
	}
	return total
}

func parse_part1(line string) ([]int, [][]int) {
	items := strings.Split(line, " ")
	lights_str := []rune(items[0][1 : len(items[0])-1])
	buttons_lst := items[1 : len(items)-1]
	lights := make([]int, len(lights_str))
	for i := range len(lights_str) {
		if lights_str[i] == '.' {
			lights[i] = 0
		} else {
			lights[i] = 1
		}
	}
	var buttons [][]int
	for _, b := range buttons_lst {
		b_str := strings.Split(b[1:len(b)-1], ",")
		var x []int
		for _, v := range b_str {
			v, _ := strconv.Atoi(v)
			x = append(x, v)
		}
		buttons = append(buttons, x)
	}
	return lights, buttons
}

func state2idx1(state []int) int {
	idx := 0
	for i := range len(state) {
		if state[i] == 1 {
			idx += int(math.Pow(2, float64(i)))
		}
	}
	return idx
}

func bfs1(final_state []int, actions [][]int) int {
	n := len(final_state)
	start_state := make([]int, n)
	var queue [][]int
	queue = append(queue, start_state)
	dist := make([]int, int(math.Pow(2, float64(n))))
	for i := range len(dist) {
		dist[i] = -1
	}
	dist[0] = 0
	for len(queue) > 0 {
		state := queue[0]
		u := state2idx1(state)
		queue = queue[1:]
		for _, action := range actions {
			// Create new state based on action
			new_state := make([]int, n)
			for i := range n {
				new_state[i] = state[i]
			}
			for _, idx := range action {
				new_state[idx] = 1 - new_state[idx]
			}

			// Early return
			if slices.Equal(new_state, final_state) {
				return dist[u] + 1
			}

			// Update dist
			v := state2idx1(new_state)
			if dist[v] == -1 {
				dist[v] = dist[u] + 1
				queue = append(queue, new_state)
			}
		}
	}
	return dist[state2idx1(final_state)]
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each machine
	total := 0
	for scanner.Scan() {
		// Parse line to get lights and buttons information
		final_state, actions := parse_part2(scanner.Text())

		// Run BFS from start state to final state
		v := get_optimal_presses(final_state, actions)
		total += v
	}
	return total
}

func parse_part2(line string) ([]int, [][]int) {
	items := strings.Split(line, " ")
	joltages_str := items[len(items)-1]
	joltages_lst := strings.Split(joltages_str[1:len(joltages_str)-1], ",")
	buttons_lst := items[1 : len(items)-1]
	joltages := make([]int, len(joltages_lst))
	for i, jolt := range joltages_lst {
		v, _ := strconv.Atoi(jolt)
		joltages[i] = v
	}
	var buttons [][]int
	for _, b := range buttons_lst {
		b_str := strings.Split(b[1:len(b)-1], ",")
		var x []int
		for _, v := range b_str {
			v, _ := strconv.Atoi(v)
			x = append(x, v)
		}
		buttons = append(buttons, x)
	}
	return joltages, buttons
}

func get_optimal_presses(final_state []int, actions [][]int) int {
	n := len(final_state)
	m := len(actions)

	// Set up variables of system
	lp := golp.NewLP(0, m)

	// Set up objective function
	objective := make([]float64, m)
	for i := range m {
		objective[i] = 1
	}
	lp.SetObjFn(objective)

	// Add the constraints to the system
	data := make([]float64, n*m)
	idx_f := func(i int, j int) int {
		return i*m + j
	}
	for button_idx, action := range actions {
		for _, counter_idx := range action {
			data[idx_f(counter_idx, button_idx)] = 1
		}
	}
	for i := range n {
		expression := make([]float64, m)
		for j := range m {
			expression[j] = data[idx_f(i, j)]
		}
		lp.AddConstraint(expression, golp.EQ, float64(final_state[i]))
	}
	for i := range m {
		lp.SetInt(i, true)
	}

	// Solve it
	lp.Solve()
	vars := lp.Variables()
	total := 0.0
	for i := 0; i < lp.NumCols(); i++ {
		total += vars[i]
	}
	return int(total)
}

func main() {
	// fmt.Println(part1(os.Args[1]))
	fmt.Println(part2(os.Args[1]))
}
