# 1. sliding window along with set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        m = set()
        for r in range(len(s)):
            while s[r] in m:
                m.remove(s[l])
                l+=1
            m.add(s[r])
            res = max(res, r-l+1)
        
        return res
            
        

# 2. Integer array        