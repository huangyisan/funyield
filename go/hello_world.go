package main

import (
	"fmt"

)

var (
	x string = "1"
	y int = 1
	z int = 0
)

var arr [10]int


func main()  {
	slice := []int {'a', 'b', 'c', 'd'}
	c := [...]int{1,2,3,4,5}
	fmt.Println(arr)
	fmt.Println(x,y,z,c,slice)
}