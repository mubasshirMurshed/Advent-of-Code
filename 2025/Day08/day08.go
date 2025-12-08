package main

import (
	"bufio"
	"cmp"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

type UnionFind struct {
	parent []int
}

func (u UnionFind) make(n int) UnionFind {
	// Set up a UF data structure
	u.parent = make([]int, n)
	for i := range n {
		u.parent[i] = -1
	}
	return u
}

func (u UnionFind) find(elem int) int {
	// Return the parent ID of elem
	if u.parent[elem] < 0 {
		return elem
	} else {
		u.parent[elem] = u.find(u.parent[elem])
		return u.parent[elem]
	}
}

func (u UnionFind) union(a, b int) {
	// Union the two trees containing a and b
	a = u.find(a)
	b = u.find(b)
	if a == b {
		return
	}
	size_a := u.parent[a]
	size_b := u.parent[b]
	if size_a > size_b {
		a, b = b, a
	}

	// Merge b as a child of a
	u.parent[b] = a
	u.parent[a] = size_a + size_b
}

type Edge struct {
	u        int
	v        int
	distance float64
}

type Vertex struct {
	id int
	x  float64
	y  float64
	z  float64
}

func part1(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	var vertices []Vertex
	for scanner.Scan() {
		var v Vertex
		line := scanner.Text()
		coords := strings.Split(line, ",")
		x, _ := strconv.Atoi(coords[0])
		v.x = float64(x)
		y, _ := strconv.Atoi(coords[1])
		v.y = float64(y)
		z, _ := strconv.Atoi(coords[2])
		v.z = float64(z)
		vertices = append(vertices, v)
	}

	// Create all edge distances
	n := len(vertices)
	var edges []Edge
	for u := range n {
		for v := u + 1; v < n; v++ {
			var e Edge
			e.u = u
			e.v = v
			e.distance = math.Pow((vertices[u].x - vertices[v].x), 2)
			e.distance += math.Pow((vertices[u].y - vertices[v].y), 2)
			e.distance += math.Pow((vertices[u].z - vertices[v].z), 2)
			edges = append(edges, e)
		}
	}

	// Set up UF for Kruskal's Algorithm
	var uf UnionFind

	// Run Kruskal's for 1000 iterations
	uf = uf.make(n)
	edgeCmp := func(a, b Edge) int {
		return cmp.Compare(a.distance, b.distance)
	}
	slices.SortFunc(edges, edgeCmp)
	for i := range 1000 {
		e := edges[i]
		uf.union(e.u, e.v)
	}
	slices.Sort(uf.parent)
	return -uf.parent[0] * -uf.parent[1] * -uf.parent[2]
}

func part2(filename string) int {
	// Open file
	file, _ := os.Open(filename)
	defer file.Close()

	// Create a new Scanner for the file
	scanner := bufio.NewScanner(file)

	// Iterate over each line
	var vertices []Vertex
	for scanner.Scan() {
		var v Vertex
		line := scanner.Text()
		coords := strings.Split(line, ",")
		x, _ := strconv.Atoi(coords[0])
		v.x = float64(x)
		y, _ := strconv.Atoi(coords[1])
		v.y = float64(y)
		z, _ := strconv.Atoi(coords[2])
		v.z = float64(z)
		vertices = append(vertices, v)
	}

	// Create all edge distances
	n := len(vertices)
	var edges []Edge
	for u := range n {
		for v := u + 1; v < n; v++ {
			var e Edge
			e.u = u
			e.v = v
			e.distance = math.Pow((vertices[u].x - vertices[v].x), 2)
			e.distance += math.Pow((vertices[u].y - vertices[v].y), 2)
			e.distance += math.Pow((vertices[u].z - vertices[v].z), 2)
			edges = append(edges, e)
		}
	}

	// Set up UF for Kruskal's Algorithm
	var uf UnionFind

	// Run Kruskal's for 1000 iterations
	count := n
	uf = uf.make(n)
	edgeCmp := func(a, b Edge) int {
		return cmp.Compare(a.distance, b.distance)
	}
	slices.SortFunc(edges, edgeCmp)
	var e Edge
	for i := range len(edges) {
		e = edges[i]
		if uf.find(e.u) != uf.find(e.v) {
			count--
			uf.union(e.u, e.v)
		}
		if count == 1 {
			break
		}
	}
	return int(vertices[e.u].x * vertices[e.v].x)
}

func main() {
	// fmt.Println(part1(os.Args[1]))
	fmt.Println(part2(os.Args[1]))
}
