class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = len(nums)+1
        if minSize == 1:
            return 1
        left = 0
        right = 0
        currSum = nums[0]

        while right<len(nums):
            if currSum<target:
                right+=1
                if right<len(nums):
                    currSum += nums[right]
            if currSum>=target:
                length = right-left+1
                if length<minSize:
                    minSize = length
                    if minSize == 1:
                        return 1
                currSum -= nums[left]
                left+=1
        return minSize if minSize<=len(nums) else 0
