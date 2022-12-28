class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        # todo 模拟每一行和每一列的下标只能出现一次，将所有点为1的坐标列出，删除重复值
        res = []
        n = len(mat)
        for i in range(n):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    res.append((i, j))
        d1 = {}
        d2 = {}
        for x,y in res:
            if d1.get(x):
                d1[x] += 1
            else:
                d1[x] = 1
            if d2.get(y):
                d2[y] += 1
            else:
                d2[y] = 1
        l1=[]
        l2=[]
        for x,y in d1.items():
            if y>=2:
                l1.append(x)
        for x,y in d2.items():
            if y>=2:
                l2.append(x)
        result=[]
        for x,y in res:
            if x not in l1 and y not in l2:
                result.append((x,y))
        return len(result)
    def numSpecial1(self, mat: list[list[int]]) -> int:
        c = 0
        row = [sum(x) for x in mat]  # 每行的和
        col = [sum(x) for x in zip(*mat)] # 每列的和
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and row[i]==1 and col[j]==1:
                    c += 1
        return c

    def numSpecial2(self, mat: list[list[int]]) -> int:
        # todo 对于这样的特殊值，将每行和算出来，若为1
        for i, row in enumerate(mat):
            cnt1 = sum(row) - (i == 0) # 每行的总和，第一行存数据，刚好等于1则不需要改变，大于等于一，则需要加上该行的值减一

            print("i=",i,"row=",row)
            print(cnt1)



            if cnt1:
                for j, x in enumerate(row):
                    if x == 1:
                        mat[0][j] += cnt1  #若j列为1，则加上改行的总数
            print(mat[0])
        return sum(x == 1 for x in mat[0])


if __name__ == '__main__':
    mat = [[0, 0, 1],
           [0, 0, 0],
           [0, 1, 0]]
    s = Solution().numSpecial2(mat)
    print(s)