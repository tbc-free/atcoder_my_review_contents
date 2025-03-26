class Fenwicktree:
    def __init__(self, n):
        self.s = [0]*n
        self.n = n
    
    def sum(self, l, r): #半開区間
        if l > r:
            print("error")
            return False
        
        sr = 0
        id = r
        while id > 0:
            sr += self.s[id-1]
            id -= id & (-id)
        
        sl = 0
        id = l
        while id > 0:
            sl += self.s[id-1]
            id -= id & (-id)
        
        return sr-sl


    def add(self, i, x):
        id = i + 1

        while id <= self.n:
            self.s[id-1] += x
            id += id & (-id)