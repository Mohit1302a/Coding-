class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count = 0
        str1 = ""

        for i in range(len(nums)):
            str1 += str(nums[i])      

        for i in range(len(str1)):
            if str1[i] == str(digit): 
                count += 1

        return count