import sys
from typing import List
nums = []
for line in sys.stdin:
    a = line.split()
    # print(int(a[0]) + int(a[1]))
    nums.extend(a)

nums.pop(0)
nums1 = list(set(nums))
nums2 = []
for n in nums1:
    try:
        nums2.append(int(n))
    except:
        pass
def fastSort(nums: List,left,right):
    if left< right:
        i = left
        j = right
        povit = nums[left]
        while i < j:
            while i<j and nums[j] >= povit:
                j -= 1
            if nums[j] < povit:
                nums[i] = nums[j]
                i += 1
            while i<j and nums[i] <= povit:
                i += 1
            if nums[i] > povit:
                nums[j] = nums[i]
                j -= 1
        nums[i] = povit
        fastSort(nums,left,i-1)
        fastSort(nums,i+1,right)
    return nums

res = fastSort(nums2,0,len(nums2)-1)
s = ""
for n in res:
    s = s+str(n)+"\n"
print(s)