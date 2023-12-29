package main

import "fmt"

// zeroval 接受一个整数值并将其设置为零，但这是值传递。
func zeroval(ival int) {
	ival = 0
}

// zeroptr 接受一个整数指针，并通过该指针将关联的值设置为零，这是指针传递。
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	// 创建一个整数变量 i，并初始化为 1
	i := 1
	fmt.Println("initial:", i)

	// 调用 zeroval 函数，将 i 传递给函数
	zeroval(i)
	fmt.Println("zeroval:", i) // 输出: 1，值传递并不影响原始值

	// 调用 zeroptr 函数，将 i 的地址传递给函数
	zeroptr(&i)
	fmt.Println("zeroptr:", i) // 输出: 0，指针传递修改了原始值

	// 打印变量 i 的地址
	fmt.Println("pointer:", &i)
}
