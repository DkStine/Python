class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        s1 = int(s1)
        s2 = int(s2)

        return str(s1 * s2)
    
k = Solution()
print(k.multiplyStrings("10", "32"))