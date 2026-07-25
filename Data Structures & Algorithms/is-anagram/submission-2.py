class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        value=[]
        for ch in s:
            value.append(ch)
        for cha in t:
            if cha in value:
                value.remove(cha) 
        if len(value)== 0:
            return True
        else:
            return False                 

        