class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftIndex = 0
        rightIndex = len(s)-1

        while leftIndex < rightIndex:
            while leftIndex < rightIndex and not s[leftIndex].isalnum():
                leftIndex+=1
            while leftIndex < rightIndex and not s[rightIndex].isalnum():
                rightIndex-=1
            if s[leftIndex].lower() != s[rightIndex].lower():
                return False
            leftIndex+=1
            rightIndex-=1
        return True
        