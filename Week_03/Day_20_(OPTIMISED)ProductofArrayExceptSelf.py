class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        lprod = 1
        rprod = 1
        for i in range(len(nums)):
            answer[i]*=lprod
            lprod*= nums[i]
            
            answer[len(nums)-1-i]*=rprod
            rprod*=nums[len(nums)-1-i]

        return answer