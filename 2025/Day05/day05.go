package main

import (
	"bufio"
	"cmp"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

type id_range struct {
	start int
	end   int
}

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	var ID_ranges []id_range
	var IDs []int
	going_over_ranges := true
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			going_over_ranges = false
			continue
		}
		if going_over_ranges {
			range_str := strings.Split(line, "-")
			start_ID, _ := strconv.Atoi(range_str[0])
			end_ID, _ := strconv.Atoi(range_str[1])
			ID_ranges = append(ID_ranges, id_range{start_ID, end_ID})
		} else {
			ID, _ := strconv.Atoi(line)
			IDs = append(IDs, ID)
		}
	}

	// Count how many of the IDs are valid
	count := 0
	for _, ID := range IDs {
		isValid := false
		for _, ID_range := range ID_ranges {
			if ID_range.start <= ID && ID <= ID_range.end {
				isValid = true
				break
			}
		}
		if isValid {
			count++
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
	var ID_ranges []id_range
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		range_str := strings.Split(line, "-")
		start_ID, _ := strconv.Atoi(range_str[0])
		end_ID, _ := strconv.Atoi(range_str[1])
		ID_ranges = append(ID_ranges, id_range{start_ID, end_ID})
	}

	// Sort the ID ranges by start ascending
	startCmp := func(a, b id_range) int {
		return cmp.Compare(a.start, b.start)
	}
	slices.SortFunc(ID_ranges, startCmp)
	var disjoint_ID_ranges []id_range
	for _, next := range ID_ranges {
		if len(disjoint_ID_ranges) == 0 {
			disjoint_ID_ranges = append(disjoint_ID_ranges, next)
		} else {
			current := disjoint_ID_ranges[len(disjoint_ID_ranges)-1]
			if next.start <= current.end {
				if next.end > current.end {
					disjoint_ID_ranges[len(disjoint_ID_ranges)-1].end = next.end
				}
			} else {
				disjoint_ID_ranges = append(disjoint_ID_ranges, next)
			}
		}
	}

	count := 0
	for _, v := range disjoint_ID_ranges {
		count += v.end - v.start + 1
	}

	return count
}

func main() {
	fmt.Println(part1(os.Args[1]))
	fmt.Println(part2(os.Args[1]))
}
