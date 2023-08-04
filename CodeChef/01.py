class Solution:
    def isBeautiful(self, n: int) -> bool:
        def get_square_sum(number):
            sq_sum = 0
            for digit in str(number):
                sq_sum += int(digit) ** 2
            return sq_sum
        
        slow = n
        fast = n
        
        while True:
            slow = get_square_sum(slow)
            fast = get_square_sum(get_square_sum(fast))
            
            if slow == fast:
                break
        
        return 1

# Example usage
solution = Solution()
n = 19  # Replace with any integer you want to check
print(solution.isBeautiful(n))