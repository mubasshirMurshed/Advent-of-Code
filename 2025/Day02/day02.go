package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

// 1. 9 2-digit invalid IDs		Sum is 11 + 22 + 33 + 44 + ... + 99 = 110 * 4.5 = 495 = series(1,9)*11
// 2. 90 4-digit invalid IDs	Sum is 1010 + 1111 + 1212 + ... + 9898 + 9999 = 11009*45 = series(10,99)*101
// 3. 900 6-digit invalid IDs	Sum is 100100 + 101101 + ... + 998998 + 999999 = 1100099*450 = series(100, 999)*1001
// Odd length IDs have 0

func series(start int, end int) int {
	return (start + end) * (end - start + 1) / 2
}

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	line := scanner.Text()

	// Split ranges
	all_ID_ranges := strings.Split(strings.TrimSpace(line), ",")

	// Iterate over all ranges and add up the invalid IDs
	sum := 0
	for _, ID_range := range all_ID_ranges {
		total := 0
		range_lst := strings.Split(ID_range, "-")
		start_ID, _ := strconv.Atoi(range_lst[0])
		end_ID, _ := strconv.Atoi(range_lst[1])

		// Grab number of digits of each
		start_digits := int(math.Log10(float64(start_ID))) + 1
		end_digits := int(math.Log10(float64(end_ID))) + 1
		var start, end int
		if start_digits%2 != 0 { // Odd
			start = int(math.Pow10(start_digits / 2))
		} else { // Even
			start = start_ID / (int(math.Pow10(start_digits / 2)))
			if start < start_ID%(int(math.Pow10(start_digits/2))) {
				start += 1
			}
		}
		start_digits /= 2

		if end_digits%2 != 0 { // Odd
			end = int(math.Pow10(end_digits/2)) - 1
		} else { // Even
			end = end_ID / (int(math.Pow10(end_digits / 2)))
			if end > end_ID%(int(math.Pow10(end_digits/2))) {
				end -= 1
			}
		}
		end_digits /= 2

		// Start and End are the series numbers. Now calculate
		// series(start, x1)*scale1 + series(x1+1, x2)*scale2 + ... + series(xN+1, end)*scaleN
		if start <= end {
			if start_digits == end_digits {
				total += series(start, end) * (int(math.Pow10(start_digits)) + 1)
			} else {
				total += series(start, int(math.Pow10(start_digits))-1) * (int(math.Pow10(start_digits)) + 1)
				total += series(int(math.Pow10(end_digits-1)), end) * (int(math.Pow10(end_digits)) + 1)
				for i := start_digits + 1; i <= end_digits-1; i += 2 {
					total += series(int(math.Pow10(i-1)), int(math.Pow10(i))-1) * (int(math.Pow10(i)) + 1)
				}
			}
		}
		sum += total
	}

	return sum
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	line := scanner.Text()

	// Split ranges
	all_ID_ranges := strings.Split(strings.TrimSpace(line), ",")

	// Iterate over all ranges and add up the invalid IDs
	sum := 0
	for _, ID_range := range all_ID_ranges {
		total := 0
		range_lst := strings.Split(ID_range, "-")
		start_ID, _ := strconv.Atoi(range_lst[0])
		end_ID, _ := strconv.Atoi(range_lst[1])
		for number := start_ID; number <= end_ID; number++ {
			// Check if number is a valid ID
			length := int(math.Log10(float64(number))) + 1
			for i := 1; i <= length/2; i++ { // i represents the chunk size to check
				if length%i == 0 && checkInvalidID(strconv.Itoa(number), i) {
					total += number
					break
				}
			}
		}
		sum += total
	}
	return sum
}

func checkInvalidID(ID_str string, chunk_size int) bool {
	// Returns true if every chunk of chunk_size of ID_str is the same
	block_ref := ID_str[0:chunk_size]
	num_blocks := len(ID_str)/chunk_size - 1
	for i := 1; i <= num_blocks; i++ {
		if ID_str[chunk_size*i:chunk_size*(i+1)] != block_ref {
			return false
		}
	}
	return true
}

func main() {
	// var filename string = "example.txt"
	var filename string = "input.txt"
	fmt.Println(part1(filename))
	fmt.Println(part2(filename))
}
