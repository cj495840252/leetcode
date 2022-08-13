import copy
"""
899. 有序队列
给定一个字符串 s 和一个整数 k 。你可以从 s 的前 k 个字母中选择一个，并把它加到字符串的末尾。

返回 在应用上述步骤的任意数量的移动后，字典上最小的字符串 。

 """


# 最小构造法，i>2时，字符串必定能升序排列
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            res = []
            i = len(s)
            while i:
                i -= 1
                s = s[1:]+s[0]
                res.append(s)
            print(res)
            return min(res)
        else:
            return ''.join(sorted(s))

def get_srt_value(s):
    res = 0
    for i in s:
        res += ord(i)
    return res

if __name__ == '__main__':
    # print(get_srt_value('abc'))
    s = Solution().orderlyQueue("cba", 1)
    print(s)

