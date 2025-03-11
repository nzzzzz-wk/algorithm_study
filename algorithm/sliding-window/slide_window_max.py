nums = [1,3,-1,-3,5,3,6,7]
k = 3

# return win max

# 滑动窗口，队列，最大值，维护单调递增队列
# win 
# loop first check element whether larger than right
# if larger, then append to queue
# loop end popleft
# return queue last element
from collections import deque
queue = deque()
for ii in range(len(nums)):
    if queue:
        if nums[ii]>queue[-1]:
            queue.append(nums[ii])
        if len(queue)>1:
            queue.popleft()
        # if ii<k: # first k element, pass popleft
            
    else:
        queue.append(nums[ii]) # first element add to queue
    if ii >=k-1:
        print(queue[0])