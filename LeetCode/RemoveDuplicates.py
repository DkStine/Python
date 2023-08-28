class Solution:
    def removeDuplicates(self, nums : list[int]) -> int:
        st = set()
        n = len(nums)

        for i in nums:
            st.add(i)

        for j in st:
            nums.append(j)

        self.nums = nums[n::]

        return len(nums)

nums = [1, 1, 2]
k = Solution()
n = k.removeDuplicates(nums)
print(n)
print(nums)