class Solution:
    def subsets(self, nums):
        result = []
        
        def backtrack(start, path):
            # 把当前的子集加入结果
            result.append(path[:])
            
            for i in range(start, len(nums)):
                # 选择：把当前元素加入子集
                path.append(nums[i])
                
                # 递归：继续构建子集
                backtrack(i + 1, path)
                
                # 回退：撤销选择
                path.pop()
        
        # 初始化回溯
        backtrack(0, [])
        return result

# Example Usage
s = Solution()
print(s.subsets([1, 2, 3]))
# DFS