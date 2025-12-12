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
	count := 0
	for scanner.Scan() {
		// line := scanner.Text()
	}
	return count
}

func part2(filename string) int {
	return 0
}

func main() {
	fmt.Println(part1(os.Args[1]))
	// fmt.Println(part2(os.Args[1]))
}
