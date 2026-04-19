class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        for i in range(n):
            current_element = nums[i]
            if(target <= current_element):
                return i
        return n         
