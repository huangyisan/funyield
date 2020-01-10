package main

type person struct {
	name string
	age int
}



func main() {
	//P := person{name:"huangyisan", age:0}
	var P person
	P.age = 0
	P.name = "yisan"
	println(P.age, P.name)
}