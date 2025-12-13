package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Shape struct {
	points [][]int
	area   int
}

type Region struct {
	height int
	width  int
	shapes []int
	area   int
}

func part1(filename string) int {
	// Open file
	file_contents, _ := os.ReadFile(filename)
	text := string(file_contents)
	text_blocks := strings.Split(text, "\n\n")
	shape_blocks := text_blocks[:len(text_blocks)-1]
	regions := process_regions(text_blocks[len(text_blocks)-1])
	shapes := process_shapes(shape_blocks)

	count := 0
	for _, r := range regions {
		// Sum up the area of the shapes requested and compare against available area
		area_requested := 0
		for s_idx, quantity := range r.shapes {
			area_requested += quantity * shapes[s_idx].area
		}
		if area_requested <= r.area {
			count++
		}
	}
	return count
}

func process_shapes(blocks []string) []Shape {
	var shapes []Shape
	for _, block := range blocks {
		var s Shape
		lines := strings.Split(block, "\n")[1:]
		for i := range len(lines) {
			for j := range len(lines[i]) {
				if lines[i][j] == '#' {
					s.points = append(s.points, []int{i, j})
					s.area += 1
				}
			}
		}
		shapes = append(shapes, s)
	}
	return shapes
}

func process_regions(text string) []Region {
	texts := strings.Split(text, "\n")
	texts = texts[:len(texts)-1]
	var regions []Region
	for _, text := range texts {
		var r Region
		t := strings.Split(text, ":")
		dims := strings.Split(t[0], "x")
		r.height, _ = strconv.Atoi(dims[0])
		r.width, _ = strconv.Atoi(dims[1])
		r.area = r.height * r.width
		numbers_str := strings.Split(t[1][1:], " ")
		for i := range len(numbers_str) {
			v, _ := strconv.Atoi(numbers_str[i])
			r.shapes = append(r.shapes, v)
		}
		regions = append(regions, r)
	}
	return regions
}

func main() {
	fmt.Println(part1(os.Args[1]))
}
