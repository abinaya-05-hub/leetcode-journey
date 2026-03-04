class Solution:
    def isPalindrome(self, x: int) -> bool:
        h=str(x)
        r=h[::-1]
        if h==r:
            return True
        else:
            return False