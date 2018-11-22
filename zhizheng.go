package main

import "fmt"

func main(){
	var x string = "2"
	p := &x
	fmt.Println(*p)
	*p = "3"
	fmt.Println(x)

	var a,b,c int
	fmt.Println(&a == &b, &b == &c, &c == nil)
	fmt.Println(&a)
}

