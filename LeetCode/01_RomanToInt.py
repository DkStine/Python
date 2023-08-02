class Solution:
    def romanToInt(self, s: str) -> int:
        map_ = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        ans = 0

        for i in range(-1, -(len(s) + 1), -1):
            x = s[i]
            if x == 'I':
                if i == -1:
                    ans += map_['I']
                else:
                    if s[i + 1] == 'V' or s[i + 1] == 'X':
                        pass
                    else:
                        ans += map_['I']
            elif x == 'V':
                if i == -(len(s)) or len(s) == 1:
                    ans += map_['V']
                else:
                    if s[i - 1] == 'I':
                        ans += 4
                    else:
                        ans += map_['V']
            elif x == 'X':
                if len(s) == 1:
                    ans += map_['X']
                elif i == -1:
                    if s[i - 1] == 'I':
                        ans += 9
                    else:
                        ans += map_['X']
                elif i == -(len(s)):
                    if s[i + 1] == 'L' or s[i + 1] == 'C':
                        pass
                    else:
                        ans += map_['X']
                else:
                    if s[i + 1] == 'L' or s[i + 1] == 'C':
                        pass
                    elif s[i - 1] == 'I':
                        ans += 9
                    else:
                        ans += map_['X']

            elif x == 'L':
                if i == -(len(s)) or len(s) == 0:
                    ans += map_['L']
                else:
                    if s[i - 1] == 'X':
                        ans += 40
                    else:
                        ans += map_['L']

            elif x == 'C':
                if len(s) == 1:
                    ans += map_['C']
                elif i == -1:
                    if s[i - 1] == 'X':
                        ans += 90
                    else:
                        ans += map_['C']
                elif i == -(len(s)):
                    if s[i + 1] == 'D' or s[i + 1] == 'M':
                        pass
                    else:
                        ans += map_['C']
                else:
                    if s[i + 1] == 'D' or s[i + 1] == 'M':
                        pass
                    elif s[i - 1] == 'X':
                        ans += 90
                    else:
                        ans += map_['C']

            elif x == 'D':
                if i == -(len(s)) or len(s) == 1:
                    ans += map_['D']
                else:
                    if s[i - 1] == 'C':
                        ans += 400
                    else:
                        ans += map_['D']

            elif x == 'M':
                if i == -(len(s)) or len(s) == 1:
                    ans += map_['M']
                else:
                    if s[i - 1] == 'C':
                        ans += 900
                    else:
                        ans += map_['M']

        return ans


#Object initiation
k = Solution()
ans = k.romanToInt("M")
print(ans)