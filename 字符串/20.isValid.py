"""
20. 有效的括号
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. 数据结构：栈
        """
        stack = [s[0]]
        if len(s) % 2 == 1:
            return False
        for i in s[1:]:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                out = stack.pop(-1)
                if i == ')' and out == '(':
                    continue
                if i == ']' and out == '[':
                    continue
                if i == '}' and out == '{':
                    continue
                return False
        if stack and stack[-1] in ['(', '[', '{']:
            return False
        return True



if __name__ == '__main__':
    s = Solution()
    stri = "()"
    res= s.isValid(stri)
    print(res)