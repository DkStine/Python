from typing import List

class Solution:
    def reverse(self,St : List[int]) -> List[int]: 
        #code here
        for i in range(len(St) - 1):
            x = St.pop()
            St.insert(i, x)

            # [4, 1, 2, 3] ==> [4, 3, 1, 2] ==> [4, 3, 2, 1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word = ""
        flag = False

        for i in s:
            word += i
            if word in wordDict:
                flag = not flag
                return True
            else:
                pass

        if flag == False:
            return False


k = Solution()
bool_out = k.wordBreak("applepenapple", ["apple", "pen"])

if bool_out:
    print("True")
else:
    print("False")