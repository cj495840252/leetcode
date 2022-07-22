"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    !!!!!!! 想不出来的
    思想：回溯，递归，找到最后一步的解决方法，将记录的数据组合。
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        官方答案
        """
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

    def letterCombinations1(self, digits: str) -> list[str]:
        """
        复写一边
        """
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []

        res1 = []
        res2 = []

        def func(index: int):
            if index == len(digits):
                res2.append("".join(res1))
            else:
                digit = digits[index]
                for i in phoneMap[digit]:
                    res1.append(i)
                    func(index + 1)
                    res1.pop()
        func(0)
        return res2

if __name__ == '__main__':
    s = Solution()
    res = s.letterCombinations1("33")
    print(res)
