# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
# 注意：整数序列中的每一项将表示为一个字符串。
#
# 示例 1:
# 输入: 1
# 输出: "1"
# 解释：这是一个基本样例。
#
# 示例 2:
# 输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而
# 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。


class Solution:
    def countAndSay(self, n: int) -> str:
        """
        主函数，控制遍历描述函数的次数
        :param n:
        :return:
        """
        # 边界处理
        if n == 1:
            return '1'

        if n == 2:
            return '11'

        result = '11'
        # 定义标志位，例如输入3，除了两个边界处理外，还需执行一次描述函数
        flag = 2
        while flag < n:
            result = self.count(result)
            flag += 1

        return result

    def count(self, input):
        """
        对上一次结果描述的函数
        :param input:
        :return:
        """
        index = []
        count = []

        # 添加第一个值
        index.append(input[0])
        count.append(1)

        for i in range(1, len(input)):
            if input[i] == input[i - 1]:
                count[-1] += 1
            else:
                index.append(input[i])
                count.append(1)

        return ''.join([str(count[i]) + index[i] for i in range(len(index))])


result = Solution()
n = 4
print(result.countAndSay(n))


