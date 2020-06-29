// leetcode 53
// Author:lyc
// 动态规划算法
package main

import (
	"fmt"
	"math"
)

func maxSubArray(nums []int) int {

	// 传入数组为空直接返回0
	if len(nums) == 0 {
		return 0
	}

	// 创建存储状态的切片，大小和输入切片一致
	result := make([]int, len(nums))
	// 初始值设为输入切片的第一个
	result[0] = nums[0]
	// 初始化最大值
	max := nums[0]

	// 遍历，比较当前值与当前值和上一次状态的值的和，取
	// 较大者存入结果切片，再和已存在的最大值比较，覆盖max
	for i := 1; i < len(nums); i++ {
		result[i] = int(math.Max(float64(result[i-1]+nums[i]), float64(nums[i])))
		max = int(math.Max(float64(result[i]), float64(max)))
	}

	return max

}

func main() {

	// 测试
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	res := maxSubArray(nums)
	fmt.Println(res)
}
