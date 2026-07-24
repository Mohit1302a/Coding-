class Solution(object):
    def minSteps(self, n):
        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        if n == 1:
            return 0

        if isPrime(n):
            return n

        if n % 2 == 0:
            return self.minSteps(n // 2) + 2

        i = 3
        while i * i <= n:
            if n % i == 0:
                return self.minSteps(n // i) + i
            i += 2