import sys
from typing import List

msg = ""
for line in sys.stdin:
    if line =="\n":
        break
    msg += line

l = msg.rstrip("\n").split("\n")
fama:List = l[1].replace("\n","").rstrip(" ").split(" ")
nums:List = l[2].replace("\n","").split(" ")
for i in range(len(nums)):
    fama[i] = int(fama[i])
    nums[i] = int(nums[i])
sumWeight = 0
for i in range(len(fama)):
    sumWeight = fama[i]*nums[i] + sumWeight
dp = [0 for i in range(sumWeight+1)] # 记录0到sumWeight是否可行
dp[0] = 1 # Weight = 0是可行的
for i in range(len(fama)):
    for j in range(nums[i]):
        k = sumWeight
        while k >= fama[i]:
            if dp[k-fama[i]]:
                dp[k] = 1
            k-=1
print(sum(dp))