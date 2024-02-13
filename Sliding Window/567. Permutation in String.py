class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False
        a  = [0]*26
        m  = [0]*26
        for i in range(len(s1)):
            a[ord(s1[i])-ord('a')]+=1
            m[ord(s2[i])-ord('a')]+=1
            
        for i in range(len(s2)-len(s1)):
            if m ==a: return True
            
            m[ord(s2[i+len(s1)])-ord('a')]+=1
            m[ord(s2[i])-ord('a')]-=1
                
        return m==a
                
            
                
        
        