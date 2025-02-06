class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0]*self.capacity
        self.size=0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
             self.resize()
            
        # insert at next empty position
        self.arr[self.size] = n
        self.size += 1   

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        arr_new = [0] * self.capacity
        
        for i in range(self.size):
            arr_new[i]=self.arr[i] 
        self.arr = arr_new
    
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity