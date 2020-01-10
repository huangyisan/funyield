package main

import "fmt"

type testFunc func(num int) bool

func isOddr(num int) bool {
	if num%2 == 0 {
		return false
	} else {
		return true
	}
}

func isEven(num int) bool {
	if num%2 == 0 {
		return true
	} else {
		return false
	}
}

func filter(num []int, f testFunc) []int{
	var result []int
	for _, value := range num {
		if f(value) {
			//println(k)
			result = append(result, value)
		}
	}
	return result
}

func main() {
	slice := []int{1,2,3,4,5,6,7,8,9,0}
	odd_result := filter(slice, isOddr)
	even_result := filter(slice, isEven)

	fmt.Println("这些是odd",odd_result)
	fmt.Println("这些是even",even_result)
}
