package main

import "fmt"

func main() {
	var a bool = false
	switch a {
	case false:
		fmt.Println(" case ==false")
		fallthrough
	case true:
		if a == false {
			break
		}
		fmt.Println("case --true")

	}
}
