import copy

class Cargo:
    def __init__(self, amount):
        self.shipment_lots = []
        for i in range(0,amount):
            self.shipment_lots.append([])
   
    def insert_row(self, input_string):
        if input_string.strip() == "": return
        i=2
        j=0
        for char in input_string:
            i+=1
            if i % 4 == 0:
                if char != " " and char not in "1234567890":
                    self.shipment_lots[j].insert(0, char)
                j+=1
                
    def tops(self):
        out = ""
        for entry in self.shipment_lots:
            out += entry[-1]
        return out
                    
    def height(self):
        i = 0
        for j in self.shipment_lots:
            if len(j) > i: i = len(j)
        return i             
    
    def __str__(self):
        h = self.height()
        p_out = ""
        for i in range(1, h+1):
            for j in self.shipment_lots:
                if len(j) <= h-i:
                    p_out += "    "
                else:
                    p_out += f"[{j[h-i]}] "
            p_out+="\n"
        for i in range(1, len(self.shipment_lots)+1):
            p_out+= f" {i}  "
        return p_out
    
    def move1(self, origin, destination, amount):
        for i in range(0, int(amount)):
            o = self.shipment_lots[int(origin)-1].pop()
            self.shipment_lots[int(destination)-1].append(o)
            
    def move2(self, origin, destination, amount):
        pos = len(self.shipment_lots[int(origin)-1])-int(amount)
        for i in range(0, int(amount)):
            o = self.shipment_lots[int(origin)-1].pop(pos)
            self.shipment_lots[int(destination)-1].append(o)
        
                    
                    
def init():
    with open("input.txt", "r") as f:
        data = []
        for entry in f:
            data.append(entry)
    c_input = []
    for entry in data:
        if not entry.startswith("m"):
            c_input.append(entry)
    C1 = Cargo(int((len(c_input[0])+1)/4))
    C2 = Cargo(int((len(c_input[0])+1)/4))
    for entry in c_input:
        data.remove(entry)
        C1.insert_row(entry)
        C2.insert_row(entry)
    return data, C1, C2


def five1(data, C):
    for entry in data:
        _, amount, _, origin, _, destination = entry.strip().split(" ")
        C.move1(origin, destination, amount)
    print(f"1) State of cargo haven after moves: \n{C}\nTop containers: {C.tops()}\n")
    
def five2(data, C):
    for entry in data:
        _, amount, _, origin, _, destination = entry.strip().split(" ")
        C.move2(origin, destination, amount)
    print(f"2) State of cargo haven after moves: \n{C}\nTop containers: {C.tops()}\n")

data, C1, C2 = init()
five1(data, C1)
five2(data, C2)