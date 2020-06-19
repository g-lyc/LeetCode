// leetcode 35
// Author:lyc
package main

import "fmt"

func searchInsert(nums []int, target int) int {

	flag := len(nums)

	for index, value := range nums {
		// 判断当前值和target相同则立即返回当前索引
		if value == target {
			return index
		}
		// 判断一旦当前值大于target也立即返回当前索引
		if value > target {
			return index
		}
	}

	// 如果所有元素都小于target，则返回插入的位置为切片的长度
	return flag

}

func main() {

	nums := []int{1, 3, 5, 6}
	target := 7

	res := searchInsert(nums, target)

	fmt.Println(res)

}
