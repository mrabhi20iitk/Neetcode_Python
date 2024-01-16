class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for i in s:
            arr[ord(i)-97]+=1
        
        for i in t:
            arr[ord(i)-97]-=1
            
        for i in arr:
            if i!=0: return False
        
        return True
    

#-----------------------------------------------
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=  len(t): return False
        m = {}
        for i in s:
            if m.get(i): m[i]+=1
            else : m[i] = 1
                
    
        for i in t:
            if m.get(i): m[i]-=1
            else:
                return False
        
        for i in m:
            if m[i]!=0 : return False
            
        return True
        