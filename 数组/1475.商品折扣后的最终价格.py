"""
todo 1475. 商品折扣后的最终价格
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。

商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。

请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
"""

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        for i in range(len(prices)-1):
            j = i + 1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
                j += 1
        return prices
    def func2(self,prices):
        # todo 解法2：单调栈，栈里面的元素是单调增的
        n = len(prices)
        ans = [0]*n  # 记录每个位置的结果，需要数组先占位
        st = [0] #最后一个元素没有折扣，先加入一个0
        for i in (n-1,-1,-1):# 从后往前遍历
            p = prices[i]
            while len(st)>1 and st[-1] > p: # 比当前值小的全部取出
                st.pop()
            ans[i] = p - st[-1]
            st.append(p)  # 入栈
        return ans


if __name__ == '__main__':
    prices = [1,2,3,4,5]
    s = Solution().finalPrices(prices)
    print(s)