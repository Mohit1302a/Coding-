class Solution(object):
    def isSameAfterReversals(self, num):
        if num%10==0 and num>=10:
            return False
        return True