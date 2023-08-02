# nums = {5,3,7,9,7,9,7,7}
# x = 7
# y = 19

# nums = list(nums)
# l = []

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         l.append([nums[i], nums[j]])

# print(l)

# count = 0
# for k in l:
#     if (x <= k[0] * k[1]) and (k[0] * k[1] <= y):
#         print(k)
#         count += 1

# print(count)

# class Solution:
#     def TotalPairs(self, nums, x, y):
#         nums = list(nums)
#         l = []

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 l.append([nums[i], nums[j]])

#         print(l)

#         count = 0
#         for k in l:
#             if (x <= k[0] * k[1]) and (k[0] * k[1] <= y):
#                 print(k)
#                 count += 1

#         return count
    

# s = Solution()
# count = s.TotalPairs({5,3,7,9,7,9,7,7}, 7, 19)

# print(count)

# count = 0
# i_list = []

# for i in nums:
#     if i not in i_list:
#         i_list.append(i)
#         j_list = []
#         for j in nums:
#             if j not in j_list:
#                 j_list.append(j)
#                 if (x <= i * j) and (i * j <= y):
#                     count += 1

# print(count)
l = [1, 3, 2, 3, 4, 1]

for i in (l[::3]):
    print(i)