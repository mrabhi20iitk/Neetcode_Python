class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lh , rh = [0]*n , [0] * n
        lh[0] = height[0]
        rh[-1] = height[-1]
        for i in range(1,n):
            lh[i] = max(lh[i-1],height[i])
            
        for i in range(n-2,-1,-1):
            rh[i] = max(rh[i+1],height[i])
            
        sum = 0
        for i in range(n):
            sum+= min(lh[i],rh[i]) - height[i]
            
        return sum
        