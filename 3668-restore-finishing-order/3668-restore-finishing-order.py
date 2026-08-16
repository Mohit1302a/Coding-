class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_set=set(friends)
        ans=[]

        for i in order:
            if i in friend_set:
                ans.append(i)

        return ans       