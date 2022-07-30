""""
题目描述
评论 (336)
题解 (427)
提交记录
593. 有效的正方形
给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。

点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。

一个 有效的正方形 有四条等边和四个等角(90度角)。
"""
import math


class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:

        return p1 != p2 and p2 != p3 and p3 != p4 and p1 != p4 and p1 != p3 and p2 != p4 and self._sin(p1, p2,
                                                                                                       p3) and self._sin(
            p1, p2, p4) and self._sin(p4, p2, p3) and self._sin(p1, p4, p3)

    def _sin(self, p1, p2, p3):
        S12 = math.sqrt(abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2)
        S13 = math.sqrt(abs(p1[0] - p3[0]) ** 2 + abs(p1[1] - p3[1]) ** 2)
        S23 = math.sqrt(abs(p3[0] - p2[0]) ** 2 + abs(p3[1] - p2[1]) ** 2)
        if S12 != S13 and S13 != S23 and S12 != S23:
            return False
        A = (S12 ** 2 + S13 ** 2 - S23 ** 2) / (2 * S12 * S13)
        B = (S23 ** 2 + S13 ** 2 - S12 ** 2) / (2 * S23 * S13)
        C = (S12 ** 2 + S23 ** 2 - S13 ** 2) / (2 * S23 * S12)
        if abs(A) < 0.0001 or abs(B) < 0.0001 or abs(C) < 0.0001:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    res = s.validSquare([0, 0], [5, 0], [5, 4], [0, 4])
    print(res)
