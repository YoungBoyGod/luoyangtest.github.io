package main

import "fmt"

func main() {
	f("1")
	fmt.Println("2")
	defer f("4")
	fmt.Println("3")

}
func f(s string) {
	fmt.Printf("s", s)
}
