import math
class Solution:
    def countPrimes(self, n: int) -> int:
        # nums = []
        count = 0
        for num in range(2,n):
            if self.isSushu(num):
                count += 1
            print(count)
        return count

    def isSushu(self,num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    def countPrimes2(self,n: int) -> int:
        flag = [1 for i in range(n)]
        count = 0
        for i in range(2,n):
            if flag[i] == 1:
                count += 1
                #if i*i < n:
                for j in range(i*2,n,i):
                    flag[j] = 0
        return count



if __name__ == '__main__':
    n = 10
    s = Solution()
    res = s.countPrimes2(5000000)
    print(res)