class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        currSum=0
        maxLen=0
        prefix={0:-1}
        for i in range(len(nums)):
            if nums[i]==1:
                currSum+=1
            else:
                currSum+=-1
            if currSum in prefix:
                length = i-prefix[currSum]
                if length>maxLen:
                    maxLen=length
            else:
                prefix[currSum]=i
        return maxLen