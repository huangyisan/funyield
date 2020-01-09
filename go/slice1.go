package main

import "fmt"

// 声明一个数组
var array = [10]byte{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
// 声明两个slice
var aSlice []byte


func main(){
	// 演示一些简便操作
	aSlice = array[:3]
	//aSlice = array[0:1]
    fmt.Printf("%c",aSlice[0])
}
