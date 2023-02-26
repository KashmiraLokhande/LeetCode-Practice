class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChar = set()
        l = 0
        maxStr = 0
        for r in range(len(s)):
            while s[r] in uniqueChar:
                uniqueChar.remove(s[l])
                l += 1
            uniqueChar.add(s[r])
            maxStr = max( maxStr, r - l + 1)
        return maxStr

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))