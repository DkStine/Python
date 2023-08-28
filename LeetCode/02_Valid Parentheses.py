class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == "(":
                if ")" in s[i + 1]:
                    continue
                else:
                    return False
            if s[i] == ")":
                if "(" in s[i - 1]:
                    continue
                else:
                    return False
            if s[i] == "{":
                if "}" in s[i + 1]:
                    continue
                else:
                    return False
            if s[i] == "}":
                if "{" in s[i - 1]:
                    continue
                else:
                    return False
            if s[i] == "[":
                if "]" in s[i + 1]:
                    continue
                else:
                    return False
            if s[i] == "]":
                if "[" in s[i - 1]:
                    continue
                else:
                    return False
                
        return True
    
k = Solution()
bo = k.isValid("(]")
print(bo)