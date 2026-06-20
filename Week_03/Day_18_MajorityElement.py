class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0    #voting technique (aka Boyer-Moore algo)
        digit = None
        for i in nums:
            if count == 0:
                digit = i
            if i == digit:
                count+=1
            else:
                count -=1
        return digit