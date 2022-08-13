"""
761. 特殊的二进制序列
特殊的二进制序列是具有以下两个性质的二进制序列：

- 0 的数量与 1 的数量相等。
- 二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。
给定一个特殊的二进制序列 S，以字符串形式表示。定义一个操作 为首先选择 S 的两个连续且非空的特殊的子串，然后将它们交换。
（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)

在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？
"""
import functools

"""
# 题目的意思是，将二进制拆分，每一个子串都满足01个数相等，
# 前一半的1个数大于0，后一半的0个数大于1
# 最后每一个能拆分出来的字串为10或者为空时最大
# 代码实现思想
    遍历字符串过程中，用一个指针保存开始位置
    用一个计数器，遇1 增1，反之减一，计数器为0时找到一个字串，s[left+1:i] 不含i
    向下递归该子串
    同层找完全部字串
    排序
"""

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        cnt = left = 0
        subs = []
        for i, ch in enumerate(s):
            if ch == '1':
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append("1" + self.makeLargestSpecial(s[left+1:i]) + "0")
                    left = i+1
        #不能用这种方法比较, 要看前几个字符的1最多
        # subs = sorted(subs,key=functools.cmp_to_key(sort_f),reverse=True)
        subs.sort(reverse=True)
        return ''.join(subs)

def sort_f(x, y):
    x = int(x)
    y = int(y)
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


def f(s):
    if len(s)<=2:
        return s
    res = []
    stack = 0
    left = 0
    for i in range(len(s)):
        if s[i] == '1':
            stack += 1
        else:
            stack -= 1
            if stack == 0:
                res.append('1'+f(s[left+1:i])+'0')
                left = i+1
    res.sort(reverse=True)
    return ''.join(res)
if __name__ == '__main__':
    s = Solution().makeLargestSpecial("101011001110011010001111100000")
    print(s)
    res = f(s)
    print(res)
