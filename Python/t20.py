# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
# 输入: "()"
# 输出: true
# 示例 2:
# 输入: "()[]{}"
# 输出: true
# 示例 3:
# 输入: "(]"
# 输出: false
# 示例 4:
# 输入: "([)]"
# 输出: false
# 示例 5:
# 输入: "{[]}"
# 输出: true



class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        dic = {'(':')','{':'}','[':']','aaa':'aaa'}

        # 构建栈结构,只能一端进出
        z = ['aaa']
        for i in s:
            if i == ' ':
                continue
            elif z[-1] in dic and i == dic[z[-1]]:
                z.pop()
            else:
                z.append(i)

        return True if z == ['aaa'] else False



#x = "()[]{}"
x = "([)]"
result = Solution()
print(result.isValid(x))




