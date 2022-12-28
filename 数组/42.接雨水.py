"""
todo  42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""
# todo: 朴素的做法是遍历，对每个下标为i的位置，求左右两边最高值，然后取最小值，与i点高度求差  O（n²）
# todo 1：动态规划，正向遍历得到所有i，左边的高度，反向遍历得到所有i右边的高度，求最小值与i点的差，时间复杂度缩减到 O（n）
# todo 2：双指针
class Solution:
    def trap(self, height: list[int]) -> int:
        # TODO 方法1
        left = []
        right = []
        maxh = 0
        for i in height:
            if maxh < i:
                maxh = i
            left.append(maxh)
        maxh = 0
        for i in range(len(height)-1,-1,-1):
            if maxh < height[i]:
                maxh = height[i]
            right.append(maxh)
        right.reverse()
        res = 0
        for i in range(len(height)):
            res += max(min(left[i], right[i]) - height[i],0)
        return res

    def trap1(self, height: list[int]) -> int:
        # todo 2.双指针,每次操作高度最小的那一边，左边最大高度，不超过右边，左边高度高于右边则，右边移动，否则接雨水
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        res = 0
        while right != left:
            left_max = max(height[left], left_max)  # 从左往右遍历，每次更新左边的最大值，保证左边高于当前高度
            right_max = max(height[right], right_max) # 保证右边最大高度，高于右边指针指向值
            if height[left] < height[right]: # 需要一个判断，每次只能走一个指针
                res += left_max - height[left]
                left += 1
            else:
                res += right_max -height[right]
                right -= 1
        return res

    def trap2(self, height: list[int]) -> int:
        # TODO 方法三：单调递减栈,横向求，栈为空时入栈，值小于栈顶的入栈。
        #  搜索到大于栈顶的元素从栈顶将小于它的值出栈，横向宽度为最后一个出栈和当前i的差值*左右最高值的小的一个减去当前高度
        if len(height)<3:
            return 0
        res = 0
        i = 0
        stack = []
        while i < len(height):
            if stack == [] or height[stack[-1]] > height[i]:  # 相等的不如栈
                stack.append(i)
                i += 1
            else:
                print(stack, i)
                while height[stack[-1]] <= height[i]:
                    t = stack.pop()
                    # 栈中只有一个值时，当前值高度且大于栈中下标对应的高度时，出栈且不累计值
                    if not stack:
                        break
                    # 要减去一个1，比如，7和3中间，只有三个数4，5，6
                    res += (i - stack[-1] - 1)*(min(height[stack[-1]],height[i])-height[t])
                stack.append(i)
                i += 1
            print(stack)
        return res



if __name__ == '__main__':
    # height = [4,2,0,3,2,5]
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(height[0:1])
    # s = Solution().trap2(height)
    # print(s)