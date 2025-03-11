from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(path,k):
            if len(path) == k:
                result.append(path[:])
                return

            for ii in range(k):
                if nums[ii] not in path:
                    path.append(nums[ii])
                    backtrack(path,k)
                    path.pop()

        backtrack([],n)
        return result

# Example Usage
s = Solution()
print(s.permute([1, 2, 3]))