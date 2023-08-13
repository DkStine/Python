import sys
sys.setrecursionlimit(10**8)

class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n==1 or n==0:
            return n
        
        return (self.nthFibonacci(n - 1) + self.nthFibonacci(n - 2)) % 1000000007
        
k = Solution()
print(k.nthFibonacci(14521))