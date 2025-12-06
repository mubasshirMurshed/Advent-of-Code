package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func operator(symbol string) func(int) int {
	switch symbol {
	case "+":
		total := 0
		return func(a int) int {
			total += a
			return total
		}
	case "*":
		total := 1
		return func(a int) int {
			total *= a
			return total
		}
	default:
		return func(a int) int {
			return 0
		}
	}
}

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	var symbols [][]string
	for scanner.Scan() {
		line := scanner.Text()
		symbols = append(symbols, strings.Fields(line))
	}

	total := 0
	rows := len(symbols)
	cols := len(symbols[0])
	var a int
	for j := range cols {
		f := operator(symbols[rows-1][j])
		for i := 0; i < rows-1; i++ {
			value, _ := strconv.Atoi(symbols[i][j])
			a = f(value)
		}
		total += a
	}
	return total
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	var symbols [][]rune
	for scanner.Scan() {
		line := scanner.Text()
		symbols = append(symbols, []rune(line))
	}

	// Go column by column creating each number and putting in an array
	// Then when the next column is all spaces, trigger the calculation, and repeat
	rows := len(symbols)
	cols := len(symbols[0])
	new_op := true
	var f func(int) int
	var a int
	var numbers []int
	total := 0
	for j := range cols {
		// If the start of a new set of numbers, then immediately grab the operator symbol
		if new_op {
			f = operator(string(symbols[rows-1][j]))
			new_op = false
		}

		// Scan jth column if it is a number or breaking space
		var number []rune
		for i := 0; i < rows-1; i++ {
			if symbols[i][j] != ' ' {
				number = append(number, symbols[i][j])
			}
		}
		if len(number) != 0 {
			// It is a number, track it
			v, _ := strconv.Atoi(string(number))
			numbers = append(numbers, v)
		}
		if len(number) == 0 || j == cols-1 {
			// Execute calculation based on the tracked numbers
			for _, v := range numbers {
				a = f(v)
			}
			total += a

			// Set up for next calculation
			new_op = true
			numbers = nil
		}
	}

	return total
}

func main() {
	// fmt.Println(part1(os.Args[1]))
	fmt.Println(part2(os.Args[1]))
}
