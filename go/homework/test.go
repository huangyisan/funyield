package main

import (
	"fmt"
)

func main() {
	dict :=map[string]int{"a":1,"b":2}
	k,err := dict["a"]
	fmt.Println(k,err)
}
