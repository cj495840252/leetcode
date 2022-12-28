import copy
import math
from typing import List


def minWindow(s: str, t: str) -> str:
    need = {}
    window = {}
    for i in t:
        if need.get(i):
            need[i] += 1
        else :
            need[i] = 1
        window[i] = 0
    left = 0
    right = 0
    valid = 0
    start = 0
    length = math.inf
    while right < len(s):
        c = s[right]
        right += 1
        if need.get(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        while valid == len(need):
            if right-left < length:
                start = left
                length = right-left
            d = s[left]
            left += 1
            if need.get(d):
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return "" if length==math.inf else s[start:start+length]


if __name__ == '__main__':
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "aa"
    t = "aa"
    res = minWindow(s,t)
    print(res)