# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]



class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 :
            for i in range(n):
                nums1[i] = nums2[i]
        elif n == 0 :
            pass
        else:
            # 设置双指针
            p1 = m - 1
            p2 = n - 1
            # 设置赋值指针
            p = m + n - 1
            
            # 当有一个指针为负时说明有一个短的list已经遍历完成
            while p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p -= 1
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p -= 1
                    p2 -= 1
            
            # 判断如果nums2里边元素还有剩余，遍历赋值给nums1相同位置
            # 如果nums1中有剩余元素，则不用处理
            if p2 >= 0:
                while p2 >= 0:
                    nums1[p2] = nums2[p2]
                    p2 -= 1


result = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
result.merge(nums1, m, nums2, n)
print(nums1)

