class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum=0
        count=0
        prefixSum={0:1}
        for i in nums:
            currSum+=i
            if (currSum-k) in prefixSum:
                count+=prefixSum[currSum-k]
            if currSum in prefixSum:
                prefixSum[currSum]+=1
            else:
                prefixSum[currSum]=1
        return count