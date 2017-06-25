# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/#/description
# accepted
# Your runtime beats 49.71 % of python submissions.
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        count = 0
        for i in nums:
            maximum = max(maximum, )
            if i == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0
        return maximum