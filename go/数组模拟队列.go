package main

import "fmt"

/*

 */
type Queue struct {
	head int
	tail int
	maxCap int
	array []int
}

func (q *Queue) isFull() bool {
	// q.tail为下标，队列最大容量需要-1
	if q.tail == q.maxCap -1  {
		fmt.Println("队列已满")
		return false
	}
	return true
}

func (q *Queue) isEmpty() bool {
	if q.head == q.tail {
		fmt.Println("队列为空")
		return false
	}
	return true
}


func (q *Queue) pushQueue(value int) {
	// 先判断队列是否满 true为不满
	if q.isFull() {
		q.tail += 1
		q.array[q.tail] = value
	}
}

func (q *Queue) popQueue() {
	// 先判断队列是否为空 true为不空
	if q.isEmpty() {
		q.head += 1
		fmt.Println("弹出元素为")
		fmt.Println(q.array[q.head])
	}
}

func (q *Queue) showQueue() {
	// 获取从head到tail+1位切片, 因为head为未知位置，所以需要从0号位进行遍历到tail的位置。
	// 需要判断是否为空
	if q.isEmpty() {
		fmt.Println("空队列")
	} else {
		for i:=0; i<q.tail;i++ {
			fmt.Println(q.array[i])
		}
	}
}

func main() {
	Q := &Queue{
		head:-1,
		tail:-1,
		maxCap:10,
	}
	Q.popQueue()
}