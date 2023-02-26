class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if hm.get(comp) is not None:
                return [hm.get(comp), i]
            else:
                hm[nums[i]] = i
            
    def main(self):
        nums = [2,7,11,15]
        target = 9
        print(self.twoSum(nums,target))
if __name__=="__main__":
    TwoSum().main()