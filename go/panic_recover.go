package main

import "os"

var user = os.Getenv("USER")

func main() {
	defer println("aaaa")
	if user == "" {
		panic("no value for $USER")
	} else{
		println(user)
	}
}
