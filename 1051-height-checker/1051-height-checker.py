class Solution(object):
    def heightChecker(self, heights):
        count = 0
        nums = sorted(heights)

        for i in range(len(nums)):
            if nums[i] != heights[i]:
                count += 1

        return count