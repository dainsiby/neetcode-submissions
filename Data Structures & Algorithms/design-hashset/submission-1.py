class MyHashSet:

    def __init__(self):
        self.newhashset=[]
        

    def add(self, key: int) -> None:
       self.newhashset.append(key)
        
    def remove(self, key: int) -> None:
        while key in self.newhashset:
            self.newhashset.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.newhashset:
            return True
        else :
            return False    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHa.remove(key)
        

