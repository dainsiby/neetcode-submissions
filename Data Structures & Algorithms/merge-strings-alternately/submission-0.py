class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        first=0
        second=0
        while first<len(word1)and second<len(word2):
            result.append(word1[first])
            result.append(word2[second])
            first+=1
            second+=1
        result.append(word1[first:])
        result.append(word2[second:]) 
        return "".join(result)  
