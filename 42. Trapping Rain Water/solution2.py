# this solution calculates water level if its negative as well, so need to check before adding to 0.

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r] 
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                # Only add it to res if its greate than 0
                currentWaterLevel = maxL - height[l]
                res += 0 if currentWaterLevel < 0 else currentWaterLevel
                maxL = max(maxL, height[l])
                
            else:
                r -= 1
                # Only add it to res if its greate than 0
                currentWaterLevel = maxR - height[r]
                res += 0 if currentWaterLevel < 0 else currentWaterLevel
                maxR = max(maxR, height[r])

        return res