class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            sorted_string = "".join(sorted(i))
            
            if sorted_string not in res:
                res[sorted_string] = []
                
            res[sorted_string].append(i)
            
        return list(res.values())
    

#-----------------------------------------------------------------
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            ss = "".join(sorted(i))
            
            if res.get(ss):
                res[ss].append(i)
            else:
                res[ss] = [i]
                
        return list(res.values())
    


#---------------------------------------------------------------------------

            