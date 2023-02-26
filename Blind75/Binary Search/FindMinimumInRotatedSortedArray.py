class Solution:
    def findMin(self, nums: list[int]) -> int:
        leastNum = nums[0]
        l, r = 0,len(nums) -1
        while r >= l:
            
            if nums[l] < nums[r]:
                leastNum = min(leastNum, nums[l])
                break
            midNum = l + (r - l) // 2
            leastNum = min(leastNum, nums[midNum])
            if nums[midNum] >= nums[l]:
                l = midNum + 1
            else:
                r = midNum - 1
        return leastNum

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(Solution().findMin(nums)) 