from typing import List


def func(S: str):
    s = S
    flag = [0 for x in range(len(s))]
    res = []

    def f(s, temp:str):
        print(res)
        if len(temp) == len(s):
            res.append(temp)
            return
        for i, ch in enumerate(s):
            if flag[i] == 1:
                continue
            else:
                flag[i] += 1
                temp += ch
                f(s, temp)

                flag[i] -= 1
                temp = temp[:-1]
    f(s,"")
    return set(res)


if __name__ == '__main__':
    S = "qqe"
    res = func(S)
    print(res)
