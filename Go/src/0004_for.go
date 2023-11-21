package main
import "fmt"
func main() {
	i :=1
	for i<= 3{
		fmt.Println(i)
		i= i+1

	}
	for i := 0; i < 7; i++ {
		fmt.Println(i)
	}

	for i := 0; i < 10; i++ {
		if i % 2==0 {
			continue
			
		}
		fmt.Println(i)
	}
}