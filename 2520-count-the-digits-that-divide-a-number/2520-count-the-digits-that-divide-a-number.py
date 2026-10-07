class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        arr = []

        for i in str(num):
            arr.append(int(i))

        for i in arr:
            if num % i == 0:
                count += 1

        return count