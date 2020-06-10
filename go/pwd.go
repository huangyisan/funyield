package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	var oriPwd []string
	var lowerMap []map[string]int
	lowerMap = make([]map[string]int, 8)

	lowerMap[0] = make(map[string]int)
	lowerMap[0]["abc"] = 2
	lowerMap[1] = make(map[string]int)
	lowerMap[1]["def"] = 3
	lowerMap[2] = make(map[string]int)
	lowerMap[2]["ghi"] = 4
	lowerMap[3] = make(map[string]int)
	lowerMap[3]["jkl"] = 5
	lowerMap[4] = make(map[string]int)
	lowerMap[4]["mno"] = 6
	lowerMap[5] = make(map[string]int)
	lowerMap[5]["pqrs"] = 7
	lowerMap[6] = make(map[string]int)
	lowerMap[6]["tuv"] = 8
	lowerMap[7] = make(map[string]int)
	lowerMap[7]["wxy"] = 9

	var strPwd string
	fmt.Println("输入密码")
	fmt.Scanln(&strPwd)
	for _,i := range []byte(strPwd) {
		if i>=48 && i<=57 {
			oriPwd = append(oriPwd, string(i))
		} else if i>=65 && i<90 {
			oriPwd = append(oriPwd, string(i+33))
		}else if i==90 {
			oriPwd = append(oriPwd, "a")
		} else if i>=97 && i<=122 {
			for _,v := range lowerMap {
				for k1,v1 :=range v{
					if strings.ContainsAny(k1, string(i)) {
						oriPwd = append(oriPwd, strconv.Itoa(v1))
					}
				}
			}
		}
	}
	newPwd := strings.Join(oriPwd,"")
	fmt.Println(newPwd)
}
