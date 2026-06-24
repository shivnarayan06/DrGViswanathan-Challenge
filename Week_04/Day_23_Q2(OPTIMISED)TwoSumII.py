class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1
        while index1<index2:
            addition = numbers[index1]+numbers[index2]
            if target == addition:
                return [index1+1, index2+1]
            elif target > addition:
                index1+=1
            else:
                index2-=1

            
            