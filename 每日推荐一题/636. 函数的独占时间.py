
"""
有一个 单线程 CPU 正在运行一个含有 n 道函数的程序。每道函数都有一个位于  0 和 n-1 之间的唯一标识符。
函数调用 存储在一个 调用栈 上 ：当一个函数调用开始时，它的标识符将会推入栈中。
而当一个函数调用结束时，它的标识符将会从栈中弹出。标识符位于栈顶的函数是 当前正在执行的函数 。
每当一个函数开始或者结束时，将会记录一条日志，包括函数标识符、是开始还是结束、以及相应的时间戳。

给你一个由日志组成的列表 logs ，其中 logs[i] 表示第 i 条日志消息，
该消息是一个按 "{function_id}:{"start" | "end"}:{timestamp}" 进行格式化的字符串。
例如，"0:start:3" 意味着标识符为 0 的函数调用在时间戳 3 的 起始开始执行 ；
而 "1:end:2" 意味着标识符为 1 的函数调用在时间戳 2 的 末尾结束执行。
注意，函数可以 调用多次，可能存在递归调用 。

函数的 独占时间 定义是在这个函数在程序所有函数调用中执行时间的总和，
调用其他函数花费的时间不算该函数的独占时间。
例如，如果一个函数被调用两次，一次调用执行 2 单位时间，另一次调用执行 1 单位时间，那么该函数的 独占时间 为 2 + 1 = 3 。

以数组形式返回每个函数的 独占时间 ，其中第 i 个下标对应的值表示标识符 i 的函数的独占时间。

"""


class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0]*n
        stack = []
        for i in logs:
            info = i.split(':')
            info[0] = int(info[0])
            info[2] = int(info[2])
            if info[1] == "start":
                if stack:
                    res[stack[-1][0]] = res[stack[-1][0]] + info[2] - stack[-1][2]
                stack.append(info)
            else:
                q = stack.pop()
                t = info[2] - q[2] + 1
                res[info[0]] = res[info[0]] + t
                if stack:
                    stack[-1][2] = info[2] + 1  # 出栈时，要修改上一个暂停程序的运行时间，为当前运行时间加1
            # print(info,"===>", stack, "===>", res)
        return res



## 默写
def fuc(n, logs):
    res = [0]*n  # n个程序，存放结果
    stack = []  # 栈
    for i in logs:
        index, status, t = i.split(':') # 分割字符串
        index = int(index)
        t = int(t)
        if status == 'start':
            if stack:
                res[stack[-1][1]] += t - stack[-1][1]   # 程序暂停，计算已经运行的时间
            stack.append([index, t])
        else:
            p = stack.pop()
            res[index] += t - p[1] + 1
            if stack:
                stack[-1][1] = t + 1
    return res


if __name__ == '__main__':
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    s = Solution().exclusiveTime(n, logs)
    print(s)

    res = fuc(n, logs)
    assert res == s