class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        validCnt = 0
        hashmap = defaultdict(int)
        cnt = 0
        l = 0
        temp=0

        for r in range(n):
            temp=l
            # print(word[l:r+1],'='*10)
            if word[r] in 'aeiou': # basic word process
                hashmap[word[r]]+=1
            else:
                cnt+=1
            if (cnt==k) & (len(hashmap)==5):
                validCnt+=1
                # print('='*10)
                # print(validCnt,word[l:r+1],cnt,hashmap,(cnt==k) , (len(hashmap)==5)) 
                
                # move temp, check subset before move l
                # move temp valid, cnt won't change, each vowel still >1
                tF = True
                tempMap = hashmap.copy()
                while tF:
                    if (word[temp] in 'aeiou') & (tempMap[word[temp]]>1):
                        validCnt+=1
                        tempMap[word[temp]] -=1
                        temp+=1
                    else:
                        tF=False
            while l<=r:
                if (cnt <= k) & (r!=n-1):
                    # print('cnt valid, move r, break here===')
                    break
                else:
                    if word[l] in 'aeiou':
                        hashmap[word[l]]-=1
                        # print('vowel-1')
                        if hashmap[word[l]]==0:
                            del hashmap[word[l]]
                    else:
                        cnt-=1
                        # print('k-1, should break',cnt,(cnt>k) & (l<=r))
                    if (cnt==k) & (len(hashmap)==5) & (l>=temp): # if temp>l, valid cnt once & moved, current l already checked
                        validCnt+=1
                        temp=l+1
                        tF = True
                        tempMap = hashmap.copy()
                        while tF:
                            if (word[temp] in 'aeiou') & (tempMap[word[temp]]>1):
                                validCnt+=1
                                tempMap[word[temp]] -=1
                                temp+=1
                            else:
                                tF=False

                    l+=1
                # print(validCnt, "<==validCnt", l,r,cnt,hashmap, word[r])

            # print('out while')
        return validCnt