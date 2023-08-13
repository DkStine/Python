class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n == 1 or n == 2:
            return 1
        else:
            return {nthFibonacci(n - 1) + nthFibonacci(n - 2)}