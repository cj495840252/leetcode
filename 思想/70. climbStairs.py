"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        斐波那契数列, 递归超时
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n-2)



    def climbStairs0(self, n: int) -> int:
        """
        通过递推公式求特征方程，求出函数
        1/sqrt(5)[( (1+sqrt(5))/2 )**n - (1-sqrt(5))/2 )**n]
        由于前n项是从0开始的，这里向前一位
        """
        sqrt_5 = math.sqrt(5)
        return round((1/sqrt_5)*(((1+sqrt_5)/2)**(n+1) - (1-sqrt_5/2)**(n+1)))

    def climbStairs1(self, n: int) -> int:
        """
        动态规划
        """
        if n == 0:
            return 0
        # if n == 1:
        #     return 1
        p = 0
        q = 1
        cur = 0
        for i in range(n):
            cur = p + q  # 保存当前结果
            p = q  # 保存前两步的结果
            q = cur  # 保存上一步结果
        return cur

    def climbStairs2(self, n: int) -> int:
        """
        矩阵快速幂：f(n) = f(n-1)+f(n-2)
        可以调用numpy的函数
        import numpy
        arr = numpy.array([[1, 1], [1, 0]])
        print(len(arr[0]))
        arr = numpy.linalg.matrix_power(arr, n)
        return arr[0][0]

        """
        arr = [[1, 1], [1, 0]]
        arr1 = [[1, 1], [1, 0]]

        for i in range(n-1):
            arr2 = [[0, 0], [0, 0]]
            arr2[0][0] = arr1[0][0]*arr[0][0] + arr1[0][1] * arr[1][0]
            arr2[0][1] = arr1[0][0]*arr[0][1] + arr1[0][1] * arr[1][1]
            arr2[1][0] = arr1[1][0]*arr[0][0] + arr1[1][1] * arr[1][0]
            arr2[1][1] = arr1[1][0]*arr[0][0] + arr1[0][1] * arr[1][1]
            arr1 = arr2
        return arr1[0][0]

if __name__ == '__main__':
    s = Solution().climbStairs0(45)
    print(s)