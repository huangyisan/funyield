package main

type Human struct {
	name string
	age int
}

type Student struct {
	Human
	sepcify string
}

type strtoint int

func main() {
	var P Student
	P.name, P.age, P.sepcify = "huangyisan", 18, "ss"
	println(P.name,P.age,P.sepcify)
	println(strtoint('a'))
}