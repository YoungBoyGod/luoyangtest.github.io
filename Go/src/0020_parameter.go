package main

import (
	"fmt"
)

func main() {
	max(1, 2)
	fmt.Println("")
	getSum(10, 11, 21, 111)
	arr := [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr)
	update(arr)

	s1 := []int{1, 2, 3, 4, 5}
	fmt.Println("s1", s1)
	update2(s1)
}

func update2(s2 []int) {
	fmt.Println("aa", s2)
	s2[0] = 1000
	s2[100] = 10000 //panic: runtime error: index out of range [100] with length 5
	fmt.Println("aaa", s2)
}
func update(arr2 [5]int) {
	fmt.Println("jieshou", arr2)
	arr2[2] = 100
	fmt.Println("xiugai", arr2)
}

func max(num1, num2 int) int {
	var result int
	if num1 > num2 {
		result = num1

	} else {
		result = num2
	}
	print(result)
	return result
}

func getSum(nums ...int) {
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
	}
	fmt.Println("sum", sum)
}
