package main
import "fmt"

func main() {
	fmt.Println("go"+"lang")
	fmt.Println(true || false)
	fmt.Println(!true)
	var a ="init"

	fmt.Println(a)
	var b,c  int = 1,2
	fmt.Println(b,c)
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
}