"""
592. 分数加减运算
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。

这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。


"""
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        超出时间限制
        """
        res_up = 0
        res_low = 1
        molecule = ''  # 分子
        denominator = ''  # 分母
        flag = 0
        for i in expression:
            if i in ['+', '-'] and denominator:
                res_up = res_up * int(denominator) + res_low * int(molecule)
                res_low = res_low * int(denominator)
                flag -= 1
                denominator = ''
                molecule = ''
            if i == '/':
                flag += 1
            if flag == 0 and i != '/':
                molecule = molecule + i
            elif flag == 1 and i not in ['/', '+', '-']:
                denominator = denominator + i
        res_up = res_up * int(denominator) + res_low * int(molecule)
        res_low = res_low * int(denominator)
        if res_up == 0:
            res_low = 1
        # 求最大公约数
        m = res_low
        n = abs(res_up)
        while m != n:
            m = m-n
            if m < n:
                m, n = n, m
        return str(int(res_up/n)) + '/' + str(int(res_low/n))

    def fractionAddition1(self, expression: str) -> str:
        denominator, numerator = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            denominator1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1
            denominator1 = sign * denominator1
            i += 1

            # 读取分母
            numerator1 = 0
            while i < n and expression[i].isdigit():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1

            denominator = denominator * numerator1 + denominator1 * numerator
            numerator *= numerator1
        if denominator == 0:
            return "0/1"
        g = gcd(abs(denominator), numerator)
        return f"{denominator // g}/{numerator // g}"



if __name__ == '__main__':
    s = Solution()
    res = s.fractionAddition1("1/3-1/2")
    print(res)
