from typing import List


def func(nums:List[int]):
    res = [] # 记录最长的序列
    temp = []
    for i,var in enumerate(nums):
        p = i-1
        if nums[p] < var or temp == []:
            temp.append(var)
            continue
        if len(temp) > len(res):
            res.clear()
            res.extend(temp)
        temp.clear()
        temp.append(var)
    return max(len(temp),len(res))

if __name__ == '__main__':
    nums = [2,1,3]
    res = func(nums)
    print(res)
