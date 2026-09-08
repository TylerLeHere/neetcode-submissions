class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.indexOfVals = {}
        

    def insert(self, val: int) -> bool:
        if val in self.indexOfVals:
            return False
        #Insert 
        self.indexOfVals[val] = len(self.vals)
        self.vals.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indexOfVals:
            return False
        
        indexToBeRemoved = self.indexOfVals[val]
        last_val = self.vals[-1]

        self.vals[indexToBeRemoved] = last_val
        self.indexOfVals[last_val] = indexToBeRemoved

        self.vals.pop()
        del self.indexOfVals[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()