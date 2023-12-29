package main

import "fmt"

func main() {
	var x int
	var y float64

	fmt.Println("input int float")
	fmt.Scanln(&x, &y)
	fmt.Printf("x:%d,y:%f", x, y)

}
