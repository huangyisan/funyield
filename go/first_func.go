package main

func get_max_num(a,b int) int{
	if a>b{
		return a
	} else if a==b{
		return a
	} else{
		return b
	}
}


func main() {
	max_num := get_max_num(1,2)
	println(max_num)
}
