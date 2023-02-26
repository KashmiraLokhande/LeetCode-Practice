class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmS, hmT = {}, {}
        
        for i in s:
            if i in hmS:
                hmS[i] += 1
            else:
                hmS[i] = 1
        for j in t:
            if j in hmT:
                hmT[j] += 1
            else:
                hmT[j] = 1
        for k in hmS:
            if hmS.get(k, 0) !=  hmT.get(k, 0):
                return False
        
        return True
    def main(self):
        # s = "anagram"
        # t = "nagaram"
        s = "rat"
        t = "car"
        print(self.isAnagram(s,t))
if __name__ == "__main__":
    ValidAnagram().main()