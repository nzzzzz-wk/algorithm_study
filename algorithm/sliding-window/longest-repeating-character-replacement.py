from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxcnt = 0
        d = defaultdict(int)
        d[s[0]]=0
        l=0
        for r in range(len(s)):
            d[s[r]]+=1

            if r-l+1>k+max(d.values()):
                d[s[l]]-=1
                l+=1
            print(s[l:r+1],d)
            maxcnt = max(maxcnt,r-l+1)
        return maxcnt
d = Solution()
s1= "BAABACD" # 5
k1 = 2
r1 = d.characterReplacement(s1,k1)
print(r1)
s2= "AABABBA" # 4
k2=1
print('=='*5)
r2 = d.characterReplacement(s2,k2)
print(r2)