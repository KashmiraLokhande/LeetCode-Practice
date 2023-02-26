class TopKFrequentElements:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        hm = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        
        for a,v in hm.items():
            freq[v].append(a)
        
        for m in range(len(freq)- 1, 0 , -1):
            for n in freq[m]:
                res.append(n)
                if len(res)== k:
                    return res
    def main(self):
        nums = [1,1,1,2,2,3]
        k = 2
        print(self.topKFrequent(nums,k))
if __name__ == "__main__":
    TopKFrequentElements().main()