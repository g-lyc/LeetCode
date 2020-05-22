# -*- conding:utf-8 -*-
#Author:lyc
import os, sys, copy

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        flag = ''
        l = []
        for i in range(len(s)):
            if s[i] not in flag:
                flag += s[i]
                l.append(len(flag))
            else:
                flag = flag[flag.index(s[i])+1:]
                flag += s[i]
                l.append(len(flag))
        if l == []:
            return 0
        else:
            return max(l)

f = Solution()
s = 'abcabcbb'
#s = 'bbbbb'
#s = 'pwwkew'
#s = "nfpdmpi"
print(f.lengthOfLongestSubstring(s))









