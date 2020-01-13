package main

import (
	"fmt"
	"math/rand"
)

func main() {
	for true {
		ran_num := gen_num()
		fmt.Printf("被猜测数字为%d\n", ran_num)
		for t := 0; t < 5; t++ {
			guess_num := input()
			if ran_num < guess_num {
				fmt.Printf("猜得太小了，还剩下%d次机会\n", 4-t)
			} else if ran_num > guess_num {
				fmt.Printf("猜得太大了，还剩下%d次机会\n", 4-t)
			} else {
				fmt.Print("猜对了")
				break
			}
			if t == 4{
				fmt.Print("太笨了\n 重新开始！")
				break
			}
		}
	}
}

func gen_num() int{
	num := rand.Intn(100)
	return num
}

func input() int{
	var input_num int
	fmt.Print("请输入一个数字\n")
	fmt.Scanln(&input_num)
	fmt.Print(input_num)
	return input_num
}
