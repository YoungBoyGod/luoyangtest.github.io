package main

import "fmt"

func main() {
	m := make(map[string]int)
	m["k1"] = 4
	m["k2"] = 22
	fmt.Println("map", m)

	v1 := m["k1"]
	fmt.Println("v1", v1)
	fmt.Println("len", len(m))

	delete(m, "k2")
	fmt.Println("delete k2", m)
	clear(m)
	fmt.Println("clear", m)
	_, prs := m["k2"]
	fmt.Println("prs", prs)

	n := map[string]int{"foo": 1, "bar": 3, "aa": 1}
	fmt.Println("map", n)
}
