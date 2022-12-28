import math


def isSushu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0 :
            return False
    return True

def func(num):
    minflag = math.inf
    n1 = 0
    for i in range(num//2):
        m = num - i
        if isSushu(m) and isSushu(i):
            l = int(math.fabs(m-i))
            if minflag > l:
                minflag = l
                n1 = i

    print(n1, num - n1)

if __name__ == '__main__':
    func(20)