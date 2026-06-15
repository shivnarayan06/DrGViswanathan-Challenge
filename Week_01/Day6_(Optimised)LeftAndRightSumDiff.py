class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        totalSum = sum(nums) 
        final = []
        for i in nums:
            rightSum = totalSum - i - leftSum
            final.append(abs(leftSum-rightSum))
            leftSum+=i

        return final
