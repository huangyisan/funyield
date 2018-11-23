package main

import "fmt"

func feibo(x,y,n int) int {
	for i:=0;i<n;i++{
		x, y = y, x+y
		fmt.Println(x,y)
	}
	return x
}

func main(){
	feibo(1,2,5)
}