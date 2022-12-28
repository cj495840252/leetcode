"""
hard
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，
例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，
能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:

有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

输出:

输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。
"""
import copy
import math
from typing import List



def test(nums)->List:
    res = []
    flag = [0 for i in range(len(nums))]
    def func(nums:List,temp:List):
        if len(temp) == len(nums):
            res.append(copy.deepcopy(temp))
            return
        for i in range(len(flag)):
            if flag[i] == 0:
                temp.append(nums[i])
                flag[i] += 1
                func(nums,temp)
                temp.pop(-1)
                flag[i] -= 1
    func(nums,[])
    return res


def isSushu(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def getSushu(nums:List[List]) -> int:
    max_count = 0
    for list1 in nums:
        temp_count = 0
        for i in range(0,len(list1),2):
            # 判断 list1[i]和list1[i+1]之和是否为素数
            t = list1[i]+list1[i+1]
            if isSushu(t):
                temp_count += 1
        max_count = max(max_count,temp_count)
    return max_count
if __name__ == '__main__':

    # 第一种方法，超时了
    # nums = [2,5,6,13]
    # tlist = test(nums)
    # res = getSushu(tlist)
    # print(res)

    # 第二种
    pass