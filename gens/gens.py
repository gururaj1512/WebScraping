class Gen:
    def __init__(self, limit):
        self.limit = limit
        self.current = None

    def next(self) -> bool:
        if self.current == None:
            self.current = 0
            return True
        
        if self.current < self.limit:
            self.current += 1
            return True
        
        return False

def gen_n(n):
    i = 0
    
    while i <= n:
        yield i
        i += 1


# gen = Gen(5)
# while gen.next():
#     print(gen.current)

for i in gen_n(5):
    print(i)