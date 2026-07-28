class Solution(object):
    def minimumOperations(self, nums):
        count=0
        for i in range(0,len(nums)):
            if nums[i]%3!=0:
                count+=1
        return count

        