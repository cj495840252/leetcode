"""
768. 最多能完成排序的块 II
这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。

arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？
"""
from collections import Counter


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        last = arr[0]
        res = []
        temp = [arr[0]]
        i = 1
        while i < len(arr):
            if arr[i] >= last and min(arr[i:]) >= last:
                last = max(arr[i], last)
                print(i, arr[i])
                res.append(temp)
                temp = []
                temp.append(arr[i])
                i += 1
            else:
                last = max(arr[i], last)
                temp.append(arr[i])
                i += 1
        res.append(temp)
        return len(res)

    def maxChunksToSorted1(self, arr: list[int]) -> int:
        """
        官解1，分段后，元素的个数和排序后的个数一样，先排序，再记录元素的频次
        """
        cnt = Counter()
        res = 0
        for x, y in zip(arr, sorted(arr)):  # x为未排序的，y为排序后的，若可以再第i次切分，那么x，y个数相等
            print(list(zip(arr, sorted(arr))))
            cnt[x] += 132
            if cnt[x] == 0:  # 个数为x，y出现次数相等时删掉
                del cnt[x]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            if len(cnt) == 0:  # 若计数器长度为0，表示该点可以切分
                res += 1
        return res

    def maxChunksToSorted2(self, arr: [int]) -> int:
        """
        官解2 ： 单调栈
        """
        stack = []
        for a in arr:
            # 这个栈是单调增的 进栈一个，先把它当作一个块
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                # 入栈的小于当前最大值，向前搜索，如果有小于该值的，那么则不是可以切分的，出栈
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
            print(stack)
        return len(stack)


def func(nums: list) -> int:
    d = {}  # 或者Counter计数器
    res = 0  # 计数
    for x, y in zip(nums, sorted(nums)):
        print(x,y)
        if d.get(x):
            d[x] += 1
        else:
            d[x] = 1
        if d.get(y):
            d[y] -= 1
        else:
            d[y] = -1
        if d.get(x) == 0:
            d.pop(x)
        if d.get(y)== 0:
            d.pop(y)
        print(d)
        if d == {}:
            res += 1
    return res


if __name__ == '__main__':
    # arr = [1, 1, 0, 0, 1]
    # arr = [0,0,1,1,1]
    arr = [0,3,0,3,2]
    # arr = [5,1,1,8,1,6,5,9,7,8]
    s = Solution().maxChunksToSorted2(arr)
    print(s)
