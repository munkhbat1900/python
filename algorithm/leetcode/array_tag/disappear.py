# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/#/description
# accepted
# Your runtime beats 97.77 % of python submissions. this one uses extra space
# without extra space solution : Your runtime beats 39.38 % of python submissions.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # with extra space solution
        # occur = [0] * len(nums)
        # for x in nums:
        #     occur[x - 1] += 1
        
        # ans = []
        # for i, x in enumerate(occur):
        #     if x == 0:
        #         ans.append(i + 1)
        # return ans

        # without extra space solution
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0 :
                nums[x - 1] = -nums[x - 1]
        
        ans = []
        for i, x in enumerate(nums):
            if x > 0:
                ans.append(i + 1)
                
        return ans