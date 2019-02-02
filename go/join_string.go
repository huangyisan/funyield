package main

import (
	"fmt"
	"strings"
	"os"
)

func main(){
	fmt.Println(strings.Join(os.Args[1:], ""))
	fmt.Println(os.Args[0])
	for k,v := range os.Args[1:] {
		fmt.Println(k,v)
	}
}

