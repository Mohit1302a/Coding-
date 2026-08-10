class Solution(object):
    def getSneakyNumbers(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                result.append(nums[i])

        return result