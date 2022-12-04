class Worker:
    start = -1
    end = -1
    w_range = -1
    def __init__(self, string):
        left, right = string.split("-")
        self.start = int(left)
        self.end = int(right)
        self.w_range = range(self.start, self.end+1)
    def includes(self, worker2):
        if worker2.start >= self.start and worker2.end <= self.end:
            return True
    def overlaps(self, worker2):
        for i in range(self.start, self.end+1):
            if i in worker2.w_range:
                return True
        return False
        

def init():
    with open("input.txt", "r") as f:
        data = []
        for lines in f:
            data.append(lines)
    return data

def four1(data):
    x = 0
    for entries in data:
        left, right = entries.split(",")
        w1 = Worker(left)
        w2 = Worker(right)
        if w1.includes(w2) or w2.includes(w1):
            x+=1
    print(f"1) Amount of fully including pairs: {x}")
    
def four2(data):
    x = 0
    for entries in data:
        left, right = entries.split(",")
        w1 = Worker(left)
        w2 = Worker(right)
        if w1.overlaps(w2):
            x+=1
    print(f"2) Amount of overlapping pairs: {x}")
    






data = init()
four1(data)
four2(data)