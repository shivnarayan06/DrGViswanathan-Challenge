class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        def nextNum(n):
            totalSum = 0
            while n>0:
                digit = n%10
                totalSum+=digit**2
                n = n//10
            return totalSum

        slow = nextNum(n)
        fast = nextNum(nextNum(n))

        while fast != 1:
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))
            if fast == slow:
                return False
        return True