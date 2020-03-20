package main

import (
	"fmt"
)

//example {"kk":{"id":11},"yy":{"id":22}}

var user_info_map map[interface{}]map[interface{}]interface{}


type userinfo struct {
	ID int
	Name string
	//Birthday time.Time
	Tel string
	Addr string
	Desc string
}

func useradd() map[interface{}]map[interface{}]interface{} {
	//dict = make(user_info_map)
	var name, tel, addr string
	//var birthday time.Time
	//var id int
	//var flag bool
	user := userinfo{}
	fmt.Println("请输入用户名:")
	fmt.Scan(&user.Name)

	for true {
		if _,ok := user_info_map[name]; ok {
			fmt.Println("该用户名已经存在，请输入其他用户名:")
			fmt.Scan(&name)
		}else{
			break
		}
	}

	fmt.Println("输入手机号:")
	fmt.Scan(&tel)

	fmt.Println("输入地址:")
	fmt.Scan(&addr)

	user_info_map = make(map[interface{}]map[interface{}]interface{})
	user_info_map[name] = make(map[interface{}]interface{})
	user_info_map[name]["addr"] = addr
	user_info_map[name]["tel"] = tel


	//user_info_map[name]["addr"] = addr
	//user_info_map[name]["tel"] = tel

	return user_info_map
}

func usermodify() map[interface{}]map[interface{}]interface{} {
	var name, tel, addr string
	fmt.Println("请输入要修改的用户:")
	fmt.Scan(&name)
	if _,ok := user_info_map[name]; ok{
		fmt.Println("输入手机号:")
		fmt.Scan(&tel)
		if tel == "\n" {
		} else{
			user_info_map[name]["tel"] = tel
		}
		fmt.Println("请输入地址:")
		fmt.Scan(&addr)
		if addr == "\n" {
			fmt.Println("修改完毕")
		} else{
			user_info_map[name]["addr"] = addr
		}
		return user_info_map

	}else{
		fmt.Println("不存在该用户")
	}
	return user_info_map
}

func userdel() map[interface{}]map[interface{}]interface{} {
	var name string
	fmt.Println("需要删除的用户:")
	fmt.Scan(&name)
	if _, ok:= user_info_map[name]; ok{
		delete(user_info_map, name)
	} else{
		fmt.Println("不存在删除用户")
	}
	return user_info_map
}

func usersearch() {
	var name string
	fmt.Println("需要查询的用户:")
	fmt.Scan(&name)
	if value,ok := user_info_map[name]; ok{
		fmt.Println(value)
	}else{
		fmt.Println("未查询到该用户")
	}
}

func main() {
	var s string
	var info map[interface{}]map[interface{}]interface{}
	for true {
		fmt.Println("用户系统\n选择要执行的内容\n a. 添加用户 \n b. 修改内容 \n c. 删除内容 \n d. 查询内容 \n")

		fmt.Scan(&s)
		if s == "a" {
			info = useradd()
		} else if s == "b" {
			info = usermodify()
		} else if s == "c" {
			info = userdel()
		} else if s == "d" {
			usersearch()
		}

		fmt.Println(info)
	}
}