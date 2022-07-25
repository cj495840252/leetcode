"""
1184. 公交站间的距离
环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 start 到目的地 destination 之间的最短距离。
"""


class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        l1 = 0
        p = start
        v1 = 0
        while True:
            l1 += distance[p]
            p = (p + 1) % len(distance)
            if p == destination:
                v1 = l1
            if p == start:
                v2 = l1 - v1
                return min(v1, v2)


if __name__ == '__main__':
    s = Solution()
    res = s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3)
    print(res)
