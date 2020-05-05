#coding:utf-8

import os
import sys

nums = [2, 7, 11, 15]
target = 9

'''class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = 0
        c = []
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] == target:
                a,b=i,i+1
        c = [a,b]
        retun c

a = Solution()
b = a.twoSum(nums,target)
print(b)'''



def twoSum(nums, target):
    map = {}
    for loc, num in enumerate(nums):
        if map.get(target - num) is not None:
            num2 = map.get(target - num)
            return [loc, num2]
        map[num] = loc


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))