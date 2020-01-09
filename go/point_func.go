package main

func plusone(num *int) int{
	*num+=1
	return *num
}

func main() {
	num := 1
	plus := plusone(&num)
	println(plus)
	println(num)
}