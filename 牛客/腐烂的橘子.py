from typing import List


def func(grid:List[List]):
    fljz = []
    goodjz = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                fljz.append((i,j))
            elif grid[i][j] == 1:
                goodjz.append((i,j))
    count = 1
    timeCount = 0
    newfl = []
    while count != 0:
        timeCount += 1
        count = 0
        for i,j in fljz:
            print(i,j,fljz)
            if (i+1,j) in goodjz:
                goodjz.remove((i+1,j))
                newfl.append((i+1,j))
                count += 1

            if (i,j+1) in goodjz:
                goodjz.remove((i,j+1))
                newfl.append((i,j+1))
                count += 1

            if (i-1,j) in goodjz:
                goodjz.remove((i-1,j))
                newfl.append((i-1,j))
                count += 1

            if (i,j-1) in goodjz:
                goodjz.remove((i,j-1))
                newfl.append((i,j-1))
                count += 1

        fljz.clear()
        fljz.extend(newfl)
        newfl.clear()

    if len(goodjz)!=0:
        return -1
    return timeCount-1











if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    res = func(grid)
    print(res)
