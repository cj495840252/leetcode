"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
"""
"""

对于一个子串而言，如果它是回文串，并且长度大于 22，那么将它首尾的两个字母去除之后，它仍然是个回文串。
例如对于字符串 ababa，如果我们已经知道 bab 是回文串，那么 ababa 一定是回文串，这是因为它的首尾两个字母都是 “a”。

所以，按长度由短到长，穷举最短的子串是否为回文
一个长为n的串，子串长度 可能为 2，3，4，... n
这里用一个n*n的二维数组记录是否为回文子串
i:左边的下标,列举1...n， for i in range(0,n)
j:右边的下标 = i+长度L - 1
从长度为2开始，求所以为2的长度子串是否为回文，记录
长度为3，判断s[i,j]是否为回文
...
长度为n时，判断s[i,i+L-1]是否为为回文

判断是否为回文：对于s[i,j], 需要满足s[i] == s[j] && s[i+1][j-1]为回文串

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # todo 动态规划, 穷举法，动态规划压缩路径
        n = len(s)
        if n <= 2:
            return s
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_len = 1
        begin = 0
        # L代表子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n): # 右边界j = i + L - 1,长度为2的子串，下标从0开始，那么j = 1
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:  # 子串长度为2 判定为True
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

    def double_extend(self,s: str):
        # todo 中心扩散
        if len(s) <= 2:
            return s
        i = j = 0
        for index in range(len(s)):
            start1, end1 = self.extend(s, index, index)
            start2, end2 = self.extend(s, index, index + 1)
            # print(start2, end2)
            if end1-start1 > j-i:
                j = end1
                i = start1
            if end2-start2 > j-i:
                j = end2
                i = start2
        print(i,j)
        return s[i:j+1]

    def extend(self, s, i, j):
        while i >= 0 and j < len(s) and s[j] == s[i]:
            i -= 1
            j += 1
        # 最后的i和j要么在边界外，要么s[i]和s[j]不相等，所以要回退到上一个
        return i+1, j-1




if __name__ == '__main__':
    s = "babad"
    s1 = "abcdcba"
    s2= "cbbd"
    # sol = Solution().longestPalindrome(s)
    sol = Solution().double_extend(s2)
    print("result==>",sol)