#using map and sorting it


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if m.get(i):
                m[i]+=1
            else:
                m[i] = 1
                
        sorted_m = sorted(m.items(), key = lambda kv : (kv[1],kv[0]),reverse=True)
        ans = []
        for i in range(k):
            ans.append(sorted_m[i][0])
        
        return ans
    
#--------------------------------Using map , 2d array---------------
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if m.get(i):
                m[i]+=1
            else:
                m[i] = 1
                
        arr = []
        for key,value in m.items():
            arr.append([value,key])
            
        arr.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(arr[i][1])
        
        return res
    

#-----------------------------------------------------------------
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = 1+count.get(i,0)
        
        for n,c in count.items():
            freq[c].append(n) 
            
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k: