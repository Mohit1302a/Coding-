class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        m = sum(nums)
        arr = []

        for num in nums:
            for i in str(num):
                arr.append(int(i))

        n = sum(arr)

        return m - n