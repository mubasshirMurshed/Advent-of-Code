package main

import (
	"bufio"
	"fmt"
	"math"
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
	var red_tiles [][2]int
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ",")
		x, _ := strconv.Atoi(line[0])
		y, _ := strconv.Atoi(line[1])
		red_tiles = append(red_tiles, [2]int{x, y})
	}

	largest_area := 0
	for i := range len(red_tiles) {
		for j := i + 1; j < len(red_tiles); j++ {
			area := (math.Abs(float64(red_tiles[i][0])-float64(red_tiles[j][0])) + 1) * (math.Abs(float64(red_tiles[i][1])-float64(red_tiles[j][1])) + 1)
			if area > float64(largest_area) {
				largest_area = int(area)
			}
		}
	}
	return largest_area
}

type line_segment struct {
	ep1          [2]int
	ep2          [2]int
	isHorizontal bool
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Parse red tile locations
	var points [][2]int
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ",")
		x, _ := strconv.Atoi(line[0])
		y, _ := strconv.Atoi(line[1])
		points = append(points, [2]int{x, y})
	}

	// Create all line segments of the concave shape
	var segments []line_segment
	for i := range len(points) {
		pos1 := points[i]
		pos2 := points[(i+1)%len(points)]
		h := pos1[1] == pos2[1]
		segments = append(segments, line_segment{pos1, pos2, h})
	}

	// Find largest area
	largest_area := 0.0
	for i := range len(points) {
		for j := i + 1; j < len(points); j++ {
			area := (math.Abs(float64(points[i][0])-float64(points[j][0])) + 1) * (math.Abs(float64(points[i][1])-float64(points[j][1])) + 1)

			// Check if the proposed rectangle is inside the shape
			if area > largest_area && isRectInPolygon(points[i], points[j], segments) {
				largest_area = area
			}
		}
	}
	return int(largest_area)
}

func isInside(segments []line_segment, point [2]int) bool {
	intersections := 0
	for _, s := range segments {
		if !s.isHorizontal {
			x := s.ep1[0]
			y_max := int(math.Max(float64(s.ep1[1]), float64(s.ep2[1])))
			y_min := int(math.Min(float64(s.ep1[1]), float64(s.ep2[1])))
			if x > point[0] && y_min < point[1] && point[1] < y_max {
				intersections++
			}
		}
	}
	return intersections%2 == 1
}

func isRectInPolygon(p1 [2]int, p2 [2]int, segments []line_segment) bool {
	// Check if the other two corners are inside
	v1 := [2]int{p1[0], p2[1]}
	v2 := [2]int{p2[0], p1[1]}
	if !(isInside(segments, v1) && isInside(segments, v2)) {
		return false
	}

	// Check if any of the line segments cuts the rectangle
	minX := int(math.Min(float64(p1[0]), float64(p2[0])))
	maxX := int(math.Max(float64(p1[0]), float64(p2[0])))
	minY := int(math.Min(float64(p1[1]), float64(p2[1])))
	maxY := int(math.Max(float64(p1[1]), float64(p2[1])))
	for _, s := range segments {
		if s.isHorizontal {
			if minY < s.ep1[1] && s.ep1[1] < maxY {
				sminX := int(math.Min(float64(s.ep1[0]), float64(s.ep2[0])))
				smaxX := int(math.Max(float64(s.ep1[0]), float64(s.ep2[0])))
				if math.Max(float64(minX), float64(sminX)) < math.Min(float64(maxX), float64(smaxX)) {
					return false
				}
			}
		} else {
			if minX < s.ep1[0] && s.ep1[0] < maxY {
				sminY := int(math.Min(float64(s.ep1[1]), float64(s.ep2[1])))
				smaxY := int(math.Max(float64(s.ep1[1]), float64(s.ep2[1])))
				if math.Max(float64(minY), float64(sminY)) < math.Min(float64(maxY), float64(smaxY)) {
					return false
				}
			}
		}
	}
	return true
}

func main() {
	fmt.Println(part1(os.Args[1]))
	fmt.Println(part2(os.Args[1]))
}
