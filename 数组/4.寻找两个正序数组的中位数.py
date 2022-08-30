"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。


"""
#  todo 通过指针合并有序数组，奇数取中间之和的一半，奇书直接取中间
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        p,q = 0, 0
        n = (len(nums1)+len(nums2))
        res = []
        while p < len(nums1) and q < len(nums2):
            if nums1[p] <= nums2[q]:
                res.append(nums1[p])
                p += 1
            else:
                res.append(nums2[q])
                q += 1
        while p < len(nums1):
            res.append(nums1[p])
            p += 1
        while q < len(nums2):
            res.append(nums2[q])
            q += 1
        print(res)
        if n%2 == 0:
            return (res[n//2]+res[n//2-1])/2
        else:
            return res[n//2]

if __name__ == '__main__':
    s = Solution().findMedianSortedArrays([1,2], [3])
    print(s)
