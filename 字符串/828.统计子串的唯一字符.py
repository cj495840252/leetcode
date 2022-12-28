import collections


def f(s:str):
    res = {}
    for i, k in enumerate(s):
        if res.get(k):
            res[k].append(i)
        else:
            res[k] = [i]
    print(res.values())
    c = 0
    for num in res.values():
        num = [-1] + num + [len(s)]
        for i in range(1, len(num) - 1):
            c += (num[i] - num[i - 1]) * (num[i + 1] - num[i])
    return c


def uniqueLetterString(s: str) -> int:
    index = collections.defaultdict(list)
    for i, c in enumerate(s):
        index[c].append(i)
    print(index.values())
    res = 0
    for arr in index.values():
        arr = [-1] + arr + [len(s)]
        print(arr)
        for i in range(1, len(arr) - 1):
            res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
    return res

if __name__ == '__main__':
    s = 'leetcode'
    res = f(s)
    print(res)
