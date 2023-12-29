package main

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		sum := getSum1(i)
		fmt.Println("sum", sum)
	}

}
func getSum1(n int) int {
	if n == 1 || n == 0 {
		return 1
	}
	return getSum1(n-1) + n
}
