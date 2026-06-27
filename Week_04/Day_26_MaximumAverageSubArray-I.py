class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        max_= currSum
        for i in range(k,len(nums)):
            currSum=currSum+nums[i]-nums[i-k]
            if currSum>max_:
                max_=currSum
        return max_/k