class Solution(object):
    def arraySign(self, nums):
        product = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            product *= nums[i]

        if product < 0:
            return -1
        else:
            return 1