from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = []
        for i in range(nums[0], nums[-1] + 1):
            ans.append(i)

        res = []
        for num in ans:
            if num not in nums:
                res.append(num)

        return res