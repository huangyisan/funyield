package main

import "fmt"

func main() {
	lecture := "Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity."
	for k, v := range lecture {
		fmt.Println(k,v)
	}
}
