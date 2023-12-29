package main

import "fmt"

func main() {
	for j := 1; j <= 9; j++ {
		for i := 1; i <= j; i++ {
			fmt.Printf("%d*%d=%d \t", i, j, i*j)
		}
		fmt.Println("")
	}

}
