class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"a", "e", "i", "o", "u"}
        currSum = 0
        for i in range(k):
            if s[i] in vowel:
                currSum+=1
        max_=currSum
        for i in range(k,len(s)):
            if s[i] in vowel:
                currSum+=1
            if s[i-k] in vowel:
                currSum-=1
            if currSum>max_:
                max_=currSum
        return max_
