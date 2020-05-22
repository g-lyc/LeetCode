# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        large_list = nums1 + nums2
        large_list.sort()

        flag = len(large_list) % 2
        media = len(large_list) // 2

        if flag == 1:

            return large_list[media]

        else:

            return (large_list[media]+large_list[media-1]) / 2



result = Solution()

nums1 = [1, 2]
nums2 = [3, 4]

print(result.findMedianSortedArrays(nums1, nums2))

# 官方答案（二分）
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

result = Solution()
print(result.findMedianSortedArrays(nums1, nums2))


