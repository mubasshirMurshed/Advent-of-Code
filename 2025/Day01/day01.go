package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	count := 0
	dial := 50
	for scanner.Scan() {
		// Get dial change
		line := scanner.Text()
		amount, _ := strconv.Atoi(strings.TrimSpace(line)[1:])

		// Process rotation
		if line[0] == 'L' {
			amount *= -1
		}
		dial = mod(dial+amount, 100)

		// Check if zero
		if dial == 0 {
			count += 1
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

	// Iterate over each line
	count := 0
	dial := 50
	var change int
	for scanner.Scan() {
		// Get dial change
		line := scanner.Text()
		amount, _ := strconv.Atoi(strings.TrimSpace(line)[1:])

		// Get rid of revolutions
		count += amount / 100
		amount = amount % 100

		// Process rotation
		if line[0] == 'L' {
			amount *= -1
		}
		new_dial := mod(dial+amount, 100)
		change = new_dial - dial

		// Check if zero
		if new_dial == 0 || (dial != 0 && change != amount) {
			count += 1
		}
		dial = new_dial
	}
	return count
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func main() {
	var filename string = "input.txt"
	fmt.Println(part1(filename))
	fmt.Println(part2(filename))
}
