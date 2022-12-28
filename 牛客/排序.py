import sys

#  HJ101.输入整型数组和排序标识
s = ""
for line in sys.stdin:
    if line == "\n":
        break
    s = s + line

a = s.split("\n")

nums = a[1].split(" ")

for i in range(1,int(a[0])):
    for j in range(0,int(a[0])-i ):
        if int(nums[j]) > int(nums[j + 1]):
            t = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = t


if a[2] == 0:
    s = ""
    for i in nums:
        s += i + " "
    print(s)
else:
    s = ""
    for i in range(len(nums) - 1, -1, -1):
        s += str(nums[i]) + " "
    print(s)