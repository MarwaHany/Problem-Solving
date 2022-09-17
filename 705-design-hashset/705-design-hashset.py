class MyHashSet:

    def __init__(self):
        self.val = []


    def add(self, key: int) -> None:
        if key not in self.val:
            self.val.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.val.pop(self.val.index(key))
        
        

    def contains(self, key: int) -> bool:
        for i in self.val:
            if i == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)