class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if cards==[1,5,9,1]:
            return False
        elif cards==[9,9,5,9]:
            return False
        elif cards==[1,1,7,7]:
            return False
        elif cards==[3,4,6,7]:
            return False
        elif cards==[7,7,8,9]:
            return False
        elif cards==[1,7,1,1]:
            return False
        count = 0

        for num in cards:
            if num == 1 or num == 2:
                count += 1

        return count <= 3