package main

import (
	"fmt"
	"unicode"
	"strings"
)

type Map map[rune]int

func (dict Map) setdefault(key rune, count int){
	if count,err:=dict[key]; !err{
		dict[key] = count
	}else{
		dict[key] = count+1
	}
}

func main() {
	str_count := Map{}
	lecture := "Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity."
	for _, v := range lecture {
		if unicode.IsUpper(v){
			v = strings.ToLower(v)
		}
		str_count.setdefault(v,1)
	}
	fmt.Print(str_count)
}