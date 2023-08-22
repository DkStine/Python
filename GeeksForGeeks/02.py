class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        # arr = []
        # ind = 0

        # for i in range(N):
        #     if A[i] == max(A):
        #         arr.append(A[i])
        #         ind = i
        #         break

        # work_list = A[ind + 1::]
        
        # for j in range(len(work_list)):
        #     if work_list[j] >= max(work_list[j::]):
        #         arr.append(work_list[j])

        # return arr                                    --> T.L.E.

        vec = []
        mx = A[-1]
        vec.append(mx)

        for i in range(-2, -(len(A) + 1), -1):
            if A[i] >= mx:
                mx = A[i]
                vec.insert(0, mx)

        return vec
    
    # --> Submitted


k = Solution()
ar = k.leaders([1,2,3,4,0], 5)
print(ar)


# a = [1, 3, 4, 5]
# n = 4

# for i in range(n):
#     print(a[i::])
#     print(max(a[i::]))
