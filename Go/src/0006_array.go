package main

import "fmt"

func main() {
	var a [6]int
	fmt.Println("emp", a)
	a[2] = 100
	fmt.Println(a)

	fmt.Println("len", len(a))

	b := [5]int{1, 2, 3, 4, 56}
	fmt.Println("bbb", b)

	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i * j
		}
	}
	fmt.Println(twoD)
}
