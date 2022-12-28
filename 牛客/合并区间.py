import copy
from typing import List


def merge(nums: List):
    nums.sort(key=lambda x: x[0])
    res = []
    interval = nums[0]
    for item in nums[1:]:
        if item[0] > interval[1]:
            print(interval)
            res.append(copy.deepcopy(interval))
            interval[0] = item[0]
            interval[1] = item[1]
        if item[0] <= interval[1] < item[1]:
            interval[1] = item[1]
    res.append(copy.deepcopy(interval))
    return res


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merge(intervals)
