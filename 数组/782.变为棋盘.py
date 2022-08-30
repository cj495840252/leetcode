"""
782. 变为棋盘
一个 n x n 的二维网络 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。
todo 不是相邻的才可交换
返回 将这个矩阵变为  “棋盘”  所需的最小移动次数 。如果不存在可行的变换，输出 -1。

“棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。
"""


class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        # todo 官方答案，不会做直接看
        """
        满足棋盘，那么每一行和第一行，10的个数要么相同要么相反
        """
        n = len(board) # 传进来的为n*n的正方形
        # 棋盘的第一行与第一列
        rowMask = colMask = 0
        for i in range(n):
            rowMask |= board[0][i] << i  # 将第一行转成二进制表示
            colMask |= board[i][0] << i  # 将第一列转成二进制表示
        reverseRowMask = ((1 << n) - 1) ^ rowMask   # 用全是1的二进制异或，反转1和0
        reverseColMask = ((1 << n) - 1) ^ colMask   # 用全是1的二进制异或，反转1和0
        rowCnt = colCnt = 0
        print(rowCnt,colMask)
        for i in range(n):
            currRowMask = currColMask = 0
            for j in range(n):
                currRowMask |= board[i][j] << j  # 将每一行转成二进制表示
                currColMask |= board[j][i] << j  # 将每一列转成二进制表示
            # 检测每一行和每一列的状态是否合法，要么和第一行要么相同，要么相反，若有一行或一列不满足，直接返回-1
            if currRowMask != rowMask and currRowMask != reverseRowMask or \
               currColMask != colMask and currColMask != reverseColMask:
                return -1
            # == 优先度最低，先算
            rowCnt += currRowMask == rowMask  # 记录与第一行相同的行数
            colCnt += currColMask == colMask  # 记录与第一列相同的列数

        def getMoves(mask: int, count: int) -> int:
            ones = self.bit_count(mask) # 记录第一行二进制中1的个数
            if n & 1: #x
                if abs(n - 2 * ones) != 1 or abs(n - 2 * count) != 1:
                    return -1
                if ones == n // 2:  # n为奇数，ones第一行1的个数，即第一行0的个数大于1的个数时，要用0开头，即奇数位变成1
                    # 偶数位变为 1 的最小交换次数 由于A:1010奇数位位0,偶数位位1 ，直接与操作，位值为1则表示需要交换，记录要交换个数
                    # todo 若是满足棋盘，那么&后必有n//2个1，缺一个则需要交换一次
                    return n // 2 - self.bit_count((mask & 0xAAAAAAAA))
                else:   # 第一行1的个数大于0的个数时，要用1开头，即偶数位变成1
                    # 奇数位变为 1 的最小交换次数
                    # todo 满足条件时，n//2 + 1 个1，
                    return (n + 1) // 2 - self.bit_count((mask & 0x55555555))
            else:
                # 如果 n 为偶数，则每一行中 1 与 0 的数目相等，且满足相邻行交替
                if ones != n // 2 or count != n // 2:
                    return -1
                # 偶数位变为 1 的最小交换次数
                count0 = n // 2 - self.bit_count((mask & 0xAAAAAAAA))
                # 奇数位变为 1 的最小交换次数
                count1 = n // 2 - self.bit_count((mask & 0x55555555))
                return min(count0, count1)
        rowMoves = getMoves(rowMask, rowCnt) # getMoves(第一行二进制，有多少行和第一行相同)
        colMoves = getMoves(colMask, colCnt)
        return -1 if rowMoves == -1 or colMoves == -1 else rowMoves + colMoves

    def bit_count(self,n:int):
        s = str(bin(n))[2:]
        c = 0
        for i in s:
            if i == '1':
                c += 1
        return c

if __name__ == '__main__':
    board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    s = Solution().movesToChessboard(board)
    print(s)
