package main

import "fmt"

func main() {
	ori_slice := []int{11,11,2,3,10,10,6,7}
	max_value := 0
	second_max_vaule := 0

	for _,v:=range ori_slice {
		if v > max_value {
			max_value = v
		}
		if v> second_max_vaule && v < max_value {
			second_max_vaule = v
		}
	}
	fmt.Printf("第二最大的值为%d，第一最大值为%d", second_max_vaule, max_value)
}
