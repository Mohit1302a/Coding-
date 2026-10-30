class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 12

        prev, curr = 12, 54  # f(1), f(2)

        for _ in range(3, n + 1):
            prev, curr = curr, (5 * curr - 2 * prev) % MOD

        return curr