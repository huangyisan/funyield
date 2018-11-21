package main

import "fmt"

func main(){
	var x string = "2"
	p := &x
	fmt.Println(*p)
	*p = "3"
	fmt.Println(x)
}

