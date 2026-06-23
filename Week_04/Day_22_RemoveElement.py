class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l] == val:
                if nums[r]!=val:
                    nums[l]=nums[r]
                    r-=1
                    l+=1
                else:
                    r-=1
            else:
                l+=1
        return l

