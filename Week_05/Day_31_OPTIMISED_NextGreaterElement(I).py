class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        info={}
        for i in nums2:
            while stack and stack[-1]<i:
                popped = stack.pop()
                info[popped]=i
            stack.append(i)
        ans=[]
        for i in nums1:
            if i in stack:
                ans.append(-1)
            else:
                ans.append(info[i])
        return ans