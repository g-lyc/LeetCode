# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<2: return nums
        i = n-1
        while i>0 and nums[i-1]>=nums[i]:
            i -= 1
        if i==0 :
            return nums.reverse()
        else:                          
            j = n-1
            while j>i-1 and nums[j]<=nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            for k in range((n-i) // 2):
                nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]


nums = [3,2,1]
result = Solution()
result.nextPermutation(nums)
print(nums)
