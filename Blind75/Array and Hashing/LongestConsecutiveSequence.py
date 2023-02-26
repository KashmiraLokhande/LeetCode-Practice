class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longestStreak = 1
        currStreak = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                if nums[i+1]-nums[i] == 1:
                    currStreak +=1
                else:
                    longestStreak = max(longestStreak, currStreak)
                    currStreak = 1
        
        return max(longestStreak, currStreak)

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))