package main

import "fmt"

//获取映射中所有key组成的切片

var k_slice []string
var v_slice []string

func main() {
	a_map := map[string]string{"a":"1","b":"2","c":"3"}

	for k,v := range a_map{
		k_slice = append(k_slice, k)
		v_slice = append(v_slice,v)

	}

	fmt.Print(k_slice)
	fmt.Print(v_slice)
}