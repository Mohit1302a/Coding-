class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr=[]
        mul=1
        add=0
        for i in str(n):
            arr.append(int(i))
        for i in arr:
            mul*=i
            add+=i   
        return mul-add