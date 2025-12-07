package main

import (
	"bufio"
	"fmt"
	"os"
)

type cell struct {
	i int
	j int
}

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Scan text as grid of runes
	var grid [][]rune
	for scanner.Scan() {
		grid = append(grid, []rune(scanner.Text()))
	}

	// Setup visited array
	rows := len(grid)
	cols := len(grid[0])
	visited := make([][]bool, rows)
	for i := range rows {
		visited[i] = make([]bool, cols)
	}

	// Find position of S
	var S cell
	for j := range cols {
		if grid[0][j] == 'S' {
			S = cell{0, j}
		}
	}

	// Establish queue and set up BFS
	visited[S.i][S.j] = true
	var queue []cell
	queue = append(queue, S)

	// Do BFS, counting if the next encountered cell is '^'
	count := 0
	for len(queue) > 0 {
		c := queue[0]
		queue = queue[1:]
		if c.i+1 == rows-1 {
			continue
		}
		if grid[c.i+1][c.j] == '.' {
			if !visited[c.i+1][c.j] {
				visited[c.i+1][c.j] = true
				queue = append(queue, cell{c.i + 1, c.j})
			}
		} else {
			count++
			if !visited[c.i+1][c.j+1] {
				visited[c.i+1][c.j+1] = true
				queue = append(queue, cell{c.i + 1, c.j + 1})
			}
			if !visited[c.i+1][c.j-1] {
				visited[c.i+1][c.j-1] = true
				queue = append(queue, cell{c.i + 1, c.j - 1})
			}
		}
	}
	return count
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Scan text as grid of runes
	var grid [][]rune
	for scanner.Scan() {
		grid = append(grid, []rune(scanner.Text()))
	}

	// Setup DP timelines array
	rows := len(grid)
	cols := len(grid[0])
	num_timelines := make([][]int, rows)
	for i := range rows {
		num_timelines[i] = make([]int, cols)
	}

	// Find position of S
	var S cell
	for j := range cols {
		if grid[0][j] == 'S' {
			S = cell{0, j}
		}
	}

	// Set up DP recursion
	var dfs func(cell) int
	dfs = func(c cell) int { // Returns the number of timelines observed from starting at cell c
		if c.i == rows-1 { // Base case
			num_timelines[c.i][c.j] = 1
		}
		if num_timelines[c.i][c.j] == 0 { // Recursive case
			if grid[c.i+1][c.j] == '.' {
				num_timelines[c.i][c.j] = dfs(cell{c.i + 1, c.j})
			} else {
				num_timelines[c.i][c.j] = dfs(cell{c.i + 1, c.j + 1}) + dfs(cell{c.i + 1, c.j - 1})
			}
		}
		return num_timelines[c.i][c.j]
	}
	return dfs(S)
}

func main() {
	fmt.Println(part1(os.Args[1]))
	fmt.Println(part2(os.Args[1]))
}
