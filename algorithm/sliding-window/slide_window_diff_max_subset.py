# 整数数组，最长连续子序列，
# 子序列中任意两个数的差不超过K，返回最长子序列的长度，若无返回0

from collections import deque

nums = [3,2,4,5,7]
k = 4
# 2 deques to store max and min, max append & popleft max[-1] , min append left & pop min[0]
# loop start 
# 1. check element max or min, update threshold
# 2. diff < k, if yes, subset_cnt+1
# 3. max_len, max(subset_cnt, max_cnt)
max_cnt = 0


for ii in range(len(nums)):
    subset_cnt = 0
    min_queue = deque([])
    max_queue = deque([])
    for jj in range(ii,len(nums)):
        if min_queue:
            num = nums[jj]
            if num > max_queue[-1]:
                max_queue.append(num)
                # max_queue.popleft()
            if num < min_queue[0]:
                min_queue.appendleft(num)
                # min_queue.pop() 
            diff = max_queue[-1] - min_queue[0]
            if diff <k:
                subset_cnt+=1
                max_cnt = max(max_cnt,subset_cnt)
            print(nums[ii],nums[jj],diff, max_queue,min_queue,max_cnt)
        else: # ii=0
            min_queue.append(nums[jj])
            max_queue.append(nums[jj])
if max_cnt>0:
    max_cnt+1