package main

import (
	"fmt"
	"time"
)

func main() {
	i :=2
	switch i {
	case 1:
		fmt.Println("111")
	case 2:
		fmt.Println("222")
	}
	switch time.Now().Weekday() {
	case time.Saturday,time.Sunday:
		fmt.Println("it weekend")
	default:
		fmt.Println("it  weekday")
	}
	whoAmI :=func (i interface{})  {
		switch t :=i.(type) {
		case bool:
			fmt.Println("bool")
		case int:
			fmt.Println("int")
		default:
			fmt.Println("oops\t",t)
		}
	}
	whoAmI(true)
	whoAmI(1)
	whoAmI("hey")

}