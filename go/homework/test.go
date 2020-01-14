package main

import (
	"fmt"
)

func main() {
	dict := make(map[interface{}]map[interface{}]interface{})
	dict[name] = make(map[interface{}]interface{})
	dict[name]["addr"] = "123"
	fmt.Println(dict)
}

