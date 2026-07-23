class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        child=0
        cokies=0
        while child<len(g) and cokies<len(s):
            if s[cokies]>=g[child]:
                child+=1
            cokies+=1
        return child
             