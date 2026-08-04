class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for word in strs:
            group="".join(sorted(word))
            if group not in result:
                result[group]=[]
            result[group].append(word)
        return list(result.values())        