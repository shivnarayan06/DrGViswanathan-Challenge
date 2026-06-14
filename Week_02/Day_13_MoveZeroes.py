class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = []
        for i in nums:
            if i != 0:
                new.append(i)
        while len(new) != len(nums):
            new.append(0)
        for i in range(len(nums)):
            nums[i] = new[i]
        