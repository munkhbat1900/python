# 561. Array Partition I
# https://leetcode.com/problems/reshape-the-matrix/#/description
# accepted
# Your runtime beats 82.32 % of python submissions.
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        h = len(nums)
        w = len(nums[0])
        if h * w != r * c:
            return nums
        ans = [[0] * c for i in range(r)]
        for i in range(r):
            for j in range(c):
                element_num = i * c + j
                ans[i][j] = nums[element_num // w][element_num - (element_num // w) * w]
        
        return ans