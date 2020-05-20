# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们
# 的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        """
        双端指针解法
        :param nums:
        :param target:
        :return:
        """

        if (not nums or len(nums)) < 3:
            return 0

        # 计算列表长度
        lenOfnums = len(nums)

        # 排序
        nums.sort()

        # 初始化一个特别大的结果值
        result = 100000

        for cur in range(lenOfnums):
            # 双端指针下标初始化
            L = cur + 1
            R = lenOfnums - 1
            while (L < R):
                sum = nums[cur] + nums[L] + nums[R]
                # 如果加和与target相等，直接返回
                if sum == target:
                    result = sum
                    return result
                # 判断如果差值小于result，则替换result的值
                if abs(target-sum) < abs(target-result):
                    result = sum
                # 指针移动
                elif sum > target:
                    R -= 1
                else:
                    L += 1
        return result


result = Solution()

nums = [-1,2,1,-4]
target = 1

print(result.threeSumClosest(nums, target))
