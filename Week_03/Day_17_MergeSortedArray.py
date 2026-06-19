class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        test = []
        p1 = 0
        p2 = 0
        while p1<m and p2<n:
            if nums1[p1]<nums2[p2]:
                test.append(nums1[p1])
                p1+=1
            else:
                test.append(nums2[p2])
                p2+=1
        while p1<m:
            test.append(nums1[p1])
            p1+=1
        while p2<n:
            test.append(nums2[p2])
            p2+=1
        nums1[:] = test
        