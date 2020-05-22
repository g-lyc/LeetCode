# -*- conding:utf-8 -*-
#Author:lyc
import os, sys


# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的
# 两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。


# 解法1 双端指针
class Solution:
    def maxArea(self, height) -> int:
        l_pointer, r_pointer = 0, len(height) - 1
        max_area = 0
        while l_pointer < r_pointer:
            max_area = max(max_area, (r_pointer - l_pointer) * min(height[l_pointer], height[r_pointer]))
            if height[l_pointer] > height[r_pointer]:
                r_pointer -= 1
            else:
                l_pointer += 1

        return max_area

# 解法2 暴力穷举（时间会超出限制）
class Solution:
    def maxArea(self, height) -> int:

        max_area = []

        if len(height) == 2:
            area = min(height)
            return area
        else:
            for i in range(len(height)-1):
                for j in range(len(height[i+1:])):
                    area = min([height[i], height[i+1:][j]]) * (j+1)
                    max_area.append(area)

        return max(max_area)



result = Solution()
#x = [1,8,6,2,5,4,8,3,7]
x = [1,2,4,3]
print(result.maxArea(x))

