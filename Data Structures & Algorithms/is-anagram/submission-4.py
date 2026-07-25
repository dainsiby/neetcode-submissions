class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        value=[]
        for ch in s:
            value.append(ch)
        for cha in t:
            if cha not in value:
                return False
            value.remove(cha) 
       
        else:
            return True                

        