"""
1422. 分割字符串的最大得分
给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。

「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。
"""

# 思想，第一次变量，记录1的个数
# 第二次遍历记录第一段0和1的个数
# 得分 = 第一段0的个数 + 1的总数 - 第一段1的个数
# 为了保证字符2不为空，遍历到n-1的位置
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        count1 = 0
        temp0 = 0
        temp1 = 0
        for i in s:
            if i == '1':
                count1 += 1
        for i in range(len(s)-1):
            if s[i] == '0':
                temp0 += 1
            else:
                temp1 += 1
            score = temp0 + count1-temp1
            max_score = max(max_score, score)
        return max_score

if __name__ == '__main__':
    s = Solution().maxScore("11111")
    print(s)