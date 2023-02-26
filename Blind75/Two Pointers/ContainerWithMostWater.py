class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        rigth = len(height) -1
        maxArea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         currArea = min(height[j], height[i]) * abs(i-j)
        #         maxArea = max(maxArea, currArea)
        
        # return maxArea
        while(left< rigth):
            currArea = min(height[left], height[rigth]) * (rigth - left)
            maxArea = max(maxArea, currArea)
            if(height[left]< height[rigth]):
                left += 1
            else:
                rigth -= 1

        return maxArea

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))