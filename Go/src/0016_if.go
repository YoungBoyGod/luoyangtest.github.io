package main

import (
	"fmt"
)

func main() {
	var a int = 5
	if a > 5 {
		fmt.Println("a>5")

	} else {
		fmt.Println("a<=5")
	}

	var b int = 93
	switch b {
	case 90:
		fmt.Println("a")
	case 80:
		fmt.Println("b")
	case 50, 60, 70:
		fmt.Println("c")
	default:
		fmt.Println("d")
	}
}
