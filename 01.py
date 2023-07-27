# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         sum = 0

#         for i in nums:
#             sum += i
#             for j in nums:
#                 if nums.index(j) != nums.index(i):
#                     sum += j
#                     if sum == target:
#                         return [nums.index(i), nums.index(j)]
#                     else:
#                         sum -= j
#             sum -= i

# p = Solution()
# print(p.twoSum([3, 3], 6))


diction = {1 : 3, 2: 6}

# t = diction.values

for i in diction:
    diction[i] += 1
    print(diction[i])