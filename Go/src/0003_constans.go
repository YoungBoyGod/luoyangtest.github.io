package main
import (
	"fmt"
	"math"
)

const s string ="constant"

func main() {
	fmt.Println(s)
	const  n = 40000000

	const d= 30e2/n
	fmt.Println(d)
	fmt.Println(math.Sin(n))
}