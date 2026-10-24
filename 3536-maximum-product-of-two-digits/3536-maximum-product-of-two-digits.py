class Solution:
    def maxProduct(self, n: int) -> int:
        a = 0
        b = 0

        while n > 0:
            digit = n % 10

            if digit > a:
                b = a
                a = digit
            elif digit > b:
                b = digit

            n //= 10

        return a * b