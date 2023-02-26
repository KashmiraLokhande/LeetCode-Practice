class containsDuplicate:
    def containsDuplicateFunc(self, nums: list[int]) -> bool:
       hs = set()
       for n in nums:
           if n in hs:
               return True
           hs.add(n)
       return False
    def main(self):
        nums = [1, 2, 3, 1]
        print(self.containsDuplicateFunc(nums))
if __name__ == "__main__":
    containsDuplicate().main()
        

