class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = []

        for i in str(n):
            digits.append(int(i))
        sum1 = sum(digits)
        for i in range(len(digits)):
            digits[i] = digits[i] * digits[i]
        sum2 = sum(digits)
        return (sum2 - sum1) >= 50