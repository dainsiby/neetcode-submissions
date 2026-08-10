class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        if s[:]==s[: :-1]:
            return True        
        while left<right:
            if s[left]!=s[right]:
                removleft=s[left+1:right+1]
                removright=s[left:right]
                return removleft[:]==removleft[: : -1] or removright[:]==removright[: :-1]
            left += 1
            right -= 1
        return True    