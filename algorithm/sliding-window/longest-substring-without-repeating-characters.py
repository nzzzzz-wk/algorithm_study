class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxcnt = 0
        n = len(s)
        ss = set()
        l = 0
        for r in range(n):
            print(r,s[l:r+1],s[r])
            while s[r] in ss:
                ss.remove(s[l])
                l+=1
            ss.add(s[r])
            maxcnt = max(maxcnt,r-l+1)
            
        return maxcnt
    
d = Solution()
# s = "abcabcbb"  # 3
# s = "bbbbb"
s = "pwwkew"  # 3
r = d.lengthOfLongestSubstring(s)
print(r)