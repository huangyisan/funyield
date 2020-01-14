package main

import (
	"fmt"
	"unicode"
	"strings"
)

type Map map[string]int

func (dict Map) setdefault(key string){
	if count,err:=dict[key]; err{
		dict[key] = count+1
	}else{
		dict[key] = 1
	}
}

func main() {

	str_count := Map{}

	lecture := "Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity."
	for _, v := range lecture {
		if unicode.IsUpper(v){
			vstring := strings.ToLower(string(v))
			str_count.setdefault(vstring,)
		}else{
			vstring := string(v)
			str_count.setdefault(vstring,)
		}
	}
	fmt.Print(str_count)
}