class Solution:
    def isPalindrome(self, s: str) -> bool:
        lef, ri = 0, len(s) -1 
        while lef < ri:
            while lef < ri and not s[lef].isalnum():
                lef += 1
            while lef < ri and not s[ri].isalnum():
                ri -= 1
            
            if s[lef].lower() != s[ri].lower():
                return False
            lef += 1
            ri -= 1
        return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))