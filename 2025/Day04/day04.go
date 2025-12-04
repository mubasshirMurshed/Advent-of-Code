package main

import (
	"bufio"
	"fmt"
	"os"
)

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	var grid [][]rune
	for scanner.Scan() {
		line := scanner.Text()
		row := []rune(line)
		grid = append(grid, row)
	}

	// Count how many '@' runes there are with < 4 adjacent '@'
	count := 0
	for i := range grid {
		for j, v := range grid[i] {
			if v == '@' && numNeighbours(grid, i, j) < 4 {
				count++
			}
		}
	}
	return count
}

func numNeighbours(grid [][]rune, i int, j int) int {
	// Returns the number of '@' signs around grid[i][j]
	var directions = [][]int{
		{-1, 0},
		{-1, 1},
		{0, 1},
		{1, 1},
		{1, 0},
		{1, -1},
		{0, -1},
		{-1, -1},
	}
	count := 0
	for _, dir := range directions {
		new_i := i + dir[0]
		new_j := j + dir[1]
		if isValid(grid, new_i, new_j) && grid[new_i][new_j] == '@' {
			count++
		}
	}
	return count
}

func isValid(grid [][]rune, i int, j int) bool {
	return 0 <= i && i < len(grid) && 0 <= j && j < len(grid[i])
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	var grid [][]rune
	for scanner.Scan() {
		line := scanner.Text()
		row := []rune(line)
		grid = append(grid, row)
	}

	var flag bool = true
	count := 0
	// Count how many '@' there are with < 4 adjacent '@' and set them to '.'
	for flag {
		flag = false
		for i := range grid {
			for j, v := range grid[i] {
				if v == '@' && numNeighbours(grid, i, j) < 4 {
					count++
					grid[i][j] = '.'
					flag = true
				}
			}
		}
	}
	return count
}

func main() {
	// var filename string = "example.txt"
	var filename string = "input.txt"
	// fmt.Println(part1(filename))
	fmt.Println(part2(filename))
}
