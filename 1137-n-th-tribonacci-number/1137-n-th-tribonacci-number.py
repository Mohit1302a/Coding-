class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1

        if n == 0:
            return a
        if n == 1 or n == 2:
            return b

        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c