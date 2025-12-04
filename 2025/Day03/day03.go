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
	total := 0
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		number := []rune(line)

		// Find the earliest largest digit
		no_of_digits := len(number)
		largest_digit := '0'
		pos := 0
		for i, v := range number {
			if v > largest_digit {
				largest_digit = v
				pos = i
			}
		}

		var maxBankValue int
		next_largest := '0'
		if pos == no_of_digits-1 { // If at end, find largest on the left of it
			for i := 0; i < pos; i++ {
				if v := number[i]; v > next_largest {
					next_largest = v
				}
			}
			maxBankValue = 10*(int(next_largest)-int('0')) + (int(largest_digit) - int('0'))
		} else { // Get the largest digit on the right of the largest
			for i := pos + 1; i < no_of_digits; i++ {
				if v := number[i]; v > next_largest {
					next_largest = v
				}
			}
			maxBankValue = 10*(int(largest_digit)-int('0')) + (int(next_largest) - int('0'))
		}
		total += maxBankValue
	}
	return total
}

func getLargestDigit(number []rune, start int, space int) (int, rune) {
	// Find largest element in number[start:] with space no of slots remaining on right side
	largest_digit := '0'
	pos := 0
	for i := start; i < len(number)-space; i++ {
		if v := number[i]; v > largest_digit {
			largest_digit = v
			pos = i
		}
	}
	return pos, largest_digit
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	total := 0
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		number := []rune(line)
		var result []rune
		pos := 0
		for i := 11; i >= 0; i-- {
			next_pos, digit := getLargestDigit(number, pos, i)
			result = append(result, digit)
			pos = next_pos + 1
		}
		maxBankValue, _ := strconv.Atoi(string(result))
		total += maxBankValue
	}
	return total
}

func main() {
	// var filename string = "example.txt"
	var filename string = "input.txt"
	// fmt.Println(part1(filename))
	fmt.Println(part2(filename))
}
