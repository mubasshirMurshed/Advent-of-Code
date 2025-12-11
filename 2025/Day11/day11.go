package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	graph := make(map[string][]string)
	for scanner.Scan() {
		vertex_info := strings.Split(scanner.Text(), ":")
		vertex := vertex_info[0]
		neighbours := strings.Split(vertex_info[1][1:], " ")
		graph[vertex] = neighbours
	}

	pathCounts := make(map[string]int)
	pathCounts["out"] = 1
	var numOfPaths func(string) int
	numOfPaths = func(u string) int {
		// Calculates the number of paths from u to "out"
		_, ok := pathCounts[u]
		if u != "out" && !ok {
			total := 0
			for _, v := range graph[u] {
				total += numOfPaths(v)
			}
			pathCounts[u] = total
		}
		return pathCounts[u]
	}
	return numOfPaths("you")
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	graph := make(map[string][]string)
	for scanner.Scan() {
		vertex_info := strings.Split(scanner.Text(), ":")
		vertex := vertex_info[0]
		neighbours := strings.Split(vertex_info[1][1:], " ")
		graph[vertex] = neighbours
	}

	// Calculate svr -> dac -> fft -> out
	// Calculate svr -> fft -> dac -> out
	// Determine chain based on which of dac->fft and fft->dac is non-zero and multiply results

	var numOfPaths func(string, string) int
	numOfPaths = func(from string, to string) int {
		pathCounts := make(map[string]int)
		pathCounts[to] = 1

		var find func(string) int
		find = func(u string) int {
			// Calculates the number of paths from u to "to" that contains dac & fft
			_, ok := pathCounts[u]
			if u != to && !ok {
				total := 0
				for _, v := range graph[u] {
					total += find(v)
				}
				pathCounts[u] = total
			}
			return pathCounts[u]
		}

		return find(from)
	}

	dac_fft := numOfPaths("dac", "fft")
	var x1, x2 string
	if dac_fft != 0 {
		x1 = "dac"
		x2 = "fft"
	} else {
		x1 = "fft"
		x2 = "dac"
	}
	return numOfPaths("svr", x1) * numOfPaths(x1, x2) * numOfPaths(x2, "out")
}

func main() {
	// fmt.Println(part1(os.Args[1]))
	fmt.Println(part2(os.Args[1]))
}
