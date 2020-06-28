// leetcode 38
// Author:lyc

package main

import (
	"fmt"
	"strconv"
)

func countAndSay(n int) string {

	// 边界处理
	if n == 1 {
		return "1"
	}

	if n == 2 {
		return "11"
	}

	// 初始化结果字符串
	result := "11"
	// 标志位，每迭代一次增加1
	flag := 2
	for {
		if flag >= n {
			break
		}
		result = count(result)
		flag += 1
	}

	return result

}

func count(input string) string {
	// 此函数为描述上一个结果
	index := []string{}
	count := []int{}

	index = append(index, string(input[0]))
	count = append(count, 1)

	for i := 1; i < len(input); i++ {
		if input[i] == input[i-1] {
			count[len(count)-1] += 1
		} else {
			index = append(index, string(input[i]))
			count = append(count, 1)
		}
	}

	result := ""
	for i := 0; i < len(index); i++ {
		result += strconv.Itoa(count[i])
		result += index[i]
	}

	return result
}

func main() {

	n := 5
	res := countAndSay(n)
	fmt.Println(res)

}
