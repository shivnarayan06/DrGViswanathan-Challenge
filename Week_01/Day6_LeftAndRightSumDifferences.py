class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        leftSum = 0
        rightSum = 0
        right = [0]
        for i in range(len(nums)-1):
            leftSum = leftSum + nums[i]
            left.append(leftSum)
    
        for j in range(1, len(nums)):
            rightSum = rightSum + nums[-j]
            right.append(rightSum)
        right.reverse()

        final =[]
        for i in range(len(nums)):
            final.append(abs(left[i] - right[i]))
        return final