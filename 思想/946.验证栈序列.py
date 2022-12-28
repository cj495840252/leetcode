"""
946. 验证栈序列
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，
只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；
否则，返回 false 。


"""

"""
思路：给定一个栈，,i指向pushed，j指向popped
当栈空或者栈中最后一个元素不等于当前j指向元素的时候，pushed[i]入栈，i后移一位
当相等时候，出栈，j后移一位
最后栈空则栈序列正确
"""
def func(pushed, popped):
    stack = []
    i = 0
    j = 0
    while j < len(popped):
        if not stack or stack[-1] != popped[j]:
            if i < len(pushed):
                stack.append(pushed[i])
            else:
                return False
            i += 1
        else:
            stack.pop()
            j += 1
    return True


if __name__ == "__main__":
    pushed = [1, 0]
    popped = [1, 0]
    print(func(pushed, popped))
