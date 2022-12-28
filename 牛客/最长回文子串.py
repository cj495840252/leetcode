import copy
import sys


def func(s, l,r):
    while l >= 0 and r<len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]



if __name__ == '__main__':

    for line in sys.stdin:
        print(line)
        s = ""
        for i in range(len(line)):
            s1 = func(line, i, i)
            s2 = func(line, i, i + 1)
            if len(s1) >= len(s2):
                s = copy.deepcopy(s1) if len(s1)>len(s) else s
            else:
                s = copy.deepcopy(s2) if len(s2) > len(s) else s
        print(s)
