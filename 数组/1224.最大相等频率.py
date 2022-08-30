"""
TODO 1224. 最大相等频率
给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：

从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
 """
"""
主要思路：
1、开辟两个数组，分别记录每一种数字的出现次数、以及每种出现次数的出现次数；
2、三个变量分别记录数字频率的最大值，最小值，以及一共出现了多少种“数字的出现次数”；
3、从数组开头依次抽取并放入新的数字，此时需要处理“1”中的数组：
    假如放入的新数字是a，那么a的出现次数加1，假设此时a的出现次数为p吧，频率p出现的次数也要加1，
    那么假如p大于1，频率p-1出现的次数要减去1（注意踩坑啊：频率0不需要任何处理，+====>看代码
    因为出现0次根本就等于没有这个数字，自始至终都没考虑过；
4、此时需要处理“2”中定义的变量：
    1）最小值min，假如a的频次此时是1，
        说明这是新加入的数字，最小值置为1；
        假如a的频次p是现在正好大于最小值min而且此时的min的频率的次数是0，
        说明这种次数不存在了，最小值需要加1；
    2）最大值max：那么a的频次大于max，max就加1；
    3）数字出现次数的种数numOfF：
        首先a的新次数的次数是1的话，numOfF加1，而如果a的次数大于1且a的旧次数的次数变成了0，
        那么numOfF需要减1；
5、接下来需要判断是否更新答案：四种情况可以更新答案：
    1）所有数频率都是1；
    2）就出现过一种数字；
    3）有两种频率，其中一种是1且出现一次；
    4）两种频率，较大的出现1次，且最大最小值相邻;
"""
from collections import Counter


class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        count = Counter()  # 记录nums中每个num出现的次数
        freq = Counter()  # 记录出现次数为某个值的个数
        maxFreq = 0
        res = 0
        for i, num in enumerate(nums):
            # 该数出现过了,那么原出现频次减一，
            # todo 1出现一次，频次{1：1}，1第二次出现1，那么出现一次的数为0，出现两次的加1，{2：1，1：0}
            if count[num]:
                freq[count[num]] -= 1  # 和该数出现次数相同的 数的个数
            count[num] += 1
            maxFreq = max(maxFreq, count[num])  # 维护最大出现次数
            freq[count[num]] += 1
            # 前面已经维护好了开头到当前节点的信息，这里动态更新最大值
            if maxFreq == 1 or \
                    freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and freq[maxFreq] == 1 \
                    or freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1:
                # 下标从零开始的，所以都需要加一
                res = max(res, i + 1)# 括号中的res是当前维护的最大值，若满足条件，i+1为当前最大值
        return res

if __name__ == '__main__':
    nums = [2, 2, 2, 1, 1, 5, 3, 3, 5]
    s = Solution().maxEqualFreq(nums)
    print(s)