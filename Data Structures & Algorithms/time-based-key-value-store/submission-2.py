class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #Does key exist in our store dictioinary, it it does not, please insert
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])


        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, []) 
        leftP = 0
        rightP = len(values) - 1

        while leftP <= rightP:
            middleIndex = (leftP + rightP) // 2
            if values[middleIndex][1] <= timestamp:
                #It is a valid value
                result = values[middleIndex][0]
                leftP = middleIndex + 1
            else:
                rightP = middleIndex - 1
        return result
                #The value is not allowed


        
