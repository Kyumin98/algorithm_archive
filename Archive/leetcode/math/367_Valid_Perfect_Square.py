class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num%num ** (1/2) == 0:
            return True
        else:
            return False
