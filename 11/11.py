class Monkey:
    def __init__(self, number, starting_items, op, test, if_true, if_false):
        self.number = int(number.split(" ")[-1].replace(":","").strip())
        self.items = []
        for entry in starting_items.split(":")[1].split(","):
            self.items.append(int(entry.strip()))
        self.te = int(test.split(" ")[-1])
        self.op = []
        for entry in op.split(" ")[-2:]:
            self.op.append(entry.strip())
        self.monkey_true = None
        self.monkey_false = None
        self.if_true = int(if_true.split(" ")[-1])
        self.if_false = int(if_false.split(" ")[-1])
        self.counter = 0
       
    def operate(self, x):
        self.counter += 1
        item = self.items.pop(0)
        if self.op[0] == "+":  
            if self.op[1] == "old":
                item += item
            else:
                item += int(self.op[1])
        elif self.op[0] == "*":  
            if self.op[1] == "old":
                item *= item
            else:
                item *= int(self.op[1])
        if x[0] == "relief":
            item = item // 3
        elif x[0] == "kgt":
            item = item % x[1]
        if item % self.te == 0:
            self.monkey_true.give(item)
        else:
            self.monkey_false.give(item)
            
    def loop(self,x):
        for i in range(len(self.items)):
            self.operate(x)
    
    def give(self, item):
        self.items.append(item) 


def init():
    with open("input.txt") as f:
        return [x for x in f]
    
def eleven1(data):
    monkeys = []
    for i in range(0, len(data)):
        if i % 7 == 0:
            m = Monkey(data[i], data[i+1], data[i+2], data[i+3], data[i+4], data[i+5])
            monkeys.append(m)
    for entry in monkeys:
        entry.monkey_true = monkeys[entry.if_true]   
        entry.monkey_false = monkeys[entry.if_false]     
    
    for i in range(0, 20):
        for entry in monkeys:
            entry.loop(("relief",0))
    monkeys.sort(key=lambda x:x.counter)
    
    print(f"1) Level of monkey business: {monkeys[-1].counter*monkeys[-2].counter}")
            
            
def eleven2(data):
    monkeys = []
    for i in range(0, len(data)):
        if i % 7 == 0:
            m = Monkey(data[i], data[i+1], data[i+2], data[i+3], data[i+4], data[i+5])
            monkeys.append(m)
    kgt = 1
    for entry in monkeys:
        entry.monkey_true = monkeys[entry.if_true]   
        entry.monkey_false = monkeys[entry.if_false]   
        kgt *= entry.te

    
    for i in range(0, 10000):
        for entry in monkeys:
            entry.loop(("kgt", kgt))
    monkeys.sort(key=lambda x:x.counter)
    
    print(f"2) Level of monkey business: {monkeys[-1].counter*monkeys[-2].counter}")
    
eleven1(init())
eleven2(init())