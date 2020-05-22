# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得
#  a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 示例：
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        """
        排序+双端指针法
        :param nums:
        :return:
        """
        # 输入为空或者元素个数小于3时直接返回[]
        if (not nums or len(nums) < 3):
            return []

        # 计算列表长度
        lenOfnums = len(nums)

        # 排序
        nums.sort()

        result = []

        for cur in range(lenOfnums):
            # 如果当前元素大于0，与后边元素相加不可能等于0，故立即返回
            if nums[cur] > 0:
                return result
            # 如果当前元素和下一个元素相等则跳过
            if (cur > 0 and nums[cur] == nums[cur - 1]):
                continue
            L = cur + 1
            R = lenOfnums - 1

            while L < R:
                if (nums[cur] + nums[L] + nums[R] == 0):
                    result.append([nums[cur] , nums[L] , nums[R]])
                    while (L < R and nums[L] == nums[L+1]):
                        L += 1
                    while (L < R and nums[R] == nums[R-1]):
                        R -= 1
                    L += 1
                    R -= 1

                elif nums[cur] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1

        return result




result = Solution()
x = [-1, 0, 1, 2, -1, -4]
print(result.threeSum(x))


