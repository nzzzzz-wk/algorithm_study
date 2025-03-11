from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(path,start,k):
            result.append(path[:])

            for ii in range(start,k):
                path.append(nums[ii])
                backtrack(path,ii+1,k)
                path.pop()
            
        backtrack([],0,n)


        return result

# Example Usage
s = Solution()
print(s.subsets([1, 2, 3]))