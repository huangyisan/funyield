package main

import (
	"fmt"
)

func main() {
	List := []int{3,2,5,7,2,1,8,9}
	new_list := maopao(List)
	fmt.Println(new_list)
}

func maopao(w_list []int) []int {
	list_len := len(w_list)
	for i:=0;i<list_len;i++{
		for j:=0; j<list_len-i-1;j++{
			if w_list[j] < w_list[j+1]{
				w_list[j+1], w_list[j] = w_list[j], w_list[j+1]
			}
		}
	}
	return w_list
}