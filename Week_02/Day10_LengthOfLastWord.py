class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        words = stripped.split()
        return len(words[-1])
 