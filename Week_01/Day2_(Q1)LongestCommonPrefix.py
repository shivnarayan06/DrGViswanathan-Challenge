class Solution:
    def longestCommonPrefix(self, strs: List[strs]) -> str:
        firstWord = strs[0]
        for i in range(len(firstWord)):
            charToCheck = firstWord[i] 
            for j in strs[1:]:
                if len(j)==i or charToCheck != j[i] :
                    return firstWord[:i]
        return firstWord