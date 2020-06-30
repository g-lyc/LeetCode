# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
# 进阶:
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        """
        动态规划解法
        :param nums:
        :return:
        """
        # 如果输入为空，直接返回
        if not nums:return 0
        result = [0 for i in range(len(nums))]
        result[0] = nums[0]
        maxV = nums[0]
        for i in range(1,len(nums)):
            result[i] = max(result[i-1]+nums[i],nums[i])
            maxV = max(result[i],maxV)
        return maxV



result = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(result.maxSubArray(nums))
