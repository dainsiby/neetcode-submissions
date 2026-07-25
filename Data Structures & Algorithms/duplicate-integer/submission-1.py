class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value=[]
        for num in nums:
            if num in value:
                return True
            else:
                value.append(num)
        return False            
            
        