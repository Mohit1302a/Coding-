class Solution(object):
    def concatWithReverse(self, nums):
        rev = nums[::-1]
        for i in range(len(rev)):
            nums.append(rev[i])
        return nums