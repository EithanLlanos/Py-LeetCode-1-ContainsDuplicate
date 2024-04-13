# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= pow(10,5)
# pow(-10,9) <= nums[i] <= pow(10,9)

####################################################################################################


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
            
            # First Attempt #
            # cont=[]
            # if len(nums) == 0 or len(nums) > pow(10,5): return
            # for i in nums:
            #     if pow(-10,9)>i or i>pow(10,9): return
            #     if not i in cont:
            #         cont.append(i)
            #     else: return 1
            # return 0

            # Second Attempt #
            # if len(nums) == 0 or len(nums) > pow(10,5): return
            # for i in nums:
            #     if pow(-10,9)>i or i>pow(10,9): return
            # if nums.count(i)!=1: return 1
            # return 0



            # Third attempt #
        if len(nums) == 0 or len(nums) > pow(10,5): return
        v={}
        for i in nums:
            v[i]=v.get(i,-1)+1
            if v[i]: return 1
        return 0