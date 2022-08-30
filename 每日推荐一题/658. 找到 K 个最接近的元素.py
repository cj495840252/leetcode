"""
 todo 658. 找到 K 个最接近的元素
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，
从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b
"""
import collections


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        res = collections.deque(arr[0:k])
        for i,v in enumerate(arr[k:]):
            if abs(res[0] - x) > abs(v - x):
                res.popleft()
                res.append(v)
        return list(res)

    def findClosestElements1(self,arr, k, x):
        # todo 双指针
        res = []
        front = len(arr)-1
        tail = len(arr)
        for i in range(len(arr)):
            if arr[i] >= x:
                front = i-1
                tail = i
                break
        print(front,tail)
        while len(res)<k:
            if front >=0 and tail < len(arr):
                if abs(arr[front]-x) <= abs(arr[tail]-x):
                    res.append(arr[front])
                    front -= 1
                    continue
                else:
                    res.append(arr[tail])
                    tail += 1
                    continue
            if front>=0:
                res.append(arr[front])
                front -= 1
                continue
            if tail <len(arr):
                res.append(arr[tail])
                tail+=1
                continue


        return sorted(res)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    arr1 = [3, 5, 8, 10]
    s = Solution().findClosestElements1(arr1, k=2, x=15)
    print(s)