package main

import "fmt"

func plus(a int, b int) int {
	return a + b
}

func plusPlus(a int, b int, c int) int {
	return a + b + c
}

func main() {
	var res, res1 int
	res = plus(1, 2)
	fmt.Println("1+2", res)
	res1 = plusPlus(1, 3, 4)
	fmt.Println("1+3+4", res1)

	for i, c := range "g2222" {
		fmt.Println(i, c)
		//字符的索引 i 和 Unicode 代码点 c
		// 'g' 的 Unicode 代码点是 103
		// 'o' 的 Unicode 代码点是 111
	}
}
