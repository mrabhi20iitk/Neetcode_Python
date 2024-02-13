class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l , r = 0 ,0 
        res = 0 
        m = {}
        maxf = 0
        for r in range(len(s)):
            m[s[r]] = 1 + m.get(s[r],0)
            
            maxf = max(maxf,m[s[r]])
            while (r-l+1) - maxf > k:
                m[s[l]] -=1
                l+=1
                
            res = max(res, r-l+1)
            
        return res
            
            
                
                
                
                
        