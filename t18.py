# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素
# a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
# 答案中不可以包含重复的四元组。
#
# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:

        if not nums or len(nums) < 4:
            return []

        numsOflens = len(nums)

        nums.sort()

        result = []

        for a in range(numsOflens - 3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for cur in range(a+1,numsOflens-2):
                if cur > a+1 and nums[cur] == nums[cur-1]:
                    continue
                L = cur + 1
                R = numsOflens - 1
                while L < R:
                    sums = nums[a] + nums[cur] + nums[L] + nums[R]
                    if sums == target:
                        result.append([nums[a],nums[cur],nums[L],nums[R]])
                        while (L < R and nums[L] == nums[L + 1]):
                            L += 1
                        while (L < R and nums[R] == nums[R - 1]):
                            R -= 1
                        L += 1
                        R -= 1
                    elif sums < target:
                        L += 1
                    else:
                        R -= 1

        return result


# 大神解法（快速）
class Solution:
    def fourSum(self, nums: [int], target: int) -> [int]:
        nums.sort()
        n = len(nums)
        res = []
        p = 0 # p, k, i, j
        while p < n - 3:  # 文中提到的条件1和条件2，可以直接跳过
            if nums[p] + 3 * nums[p + 1] > target: break
            if nums[p] + 3 * nums[-1] < target:
                while p < n - 4 and nums[p] == nums[p + 1]: p += 1
                p += 1
                continue
            k = p + 1
            while k < n - 2:   # k 和 p 的判断是一样的
                if nums[p] + nums[k] + 2 * nums[k + 1] > target: break
                if nums[p] + nums[k] + 2 * nums[-1] < target:
                    while k < n - 3 and nums[k] == nums[k + 1]:
                        k += 1
                    k += 1
                    continue
                i = k + 1
                j = n - 1
                new_target = target - nums[p] - nums[k]
                while i < j:
                    if nums[i] + nums[j] > new_target: j -= 1
                    elif nums[i] + nums[j] < new_target: i += 1
                    else:
                        res.append([nums[p],nums[k],nums[i],nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]: i += 1 # 避免结果重复
                        while i < j and nums[j] == nums[j + 1]: j -= 1 # 避免结果重复
                while k < n - 3 and nums[k] == nums[k + 1]: k += 1
                k += 1
            while p < n - 4 and nums[p] == nums[p + 1]: p += 1
            p += 1
        return res


result = Solution()
#nums = [1, 0, -1, 0, -2, 2]
nums = [0,0,0,0]
target = 0
print(result.fourSum(nums, target))








