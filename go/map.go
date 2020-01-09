package main

import "fmt"

var numbers map[string]string


func main(){
	rating := map[string]float32{"C":5, "Go":4.5, "Python":4.5, "C++":2 }
	_,ok := rating["c#"]
	if ok {
		fmt.Println("123")
	}else{
		fmt.Println("456")
	}

	numbers = make(map[string]string)
	numbers["a"] = "a"
	numbers["b"] = "b"
	numbers["c"] = "c"
	fmt.Println(numbers["a"])
	delete(rating,"Python")
}
