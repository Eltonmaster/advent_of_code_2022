
class Node:
    def __init__(self, name, type,  parent, size=0):
        self.name = name
        self.type = type
        self.parent = parent
        self.children = []
        self.size = size
        self.level = self.get_level()
        if self.parent != None:     
            self.parent.children.append(self)
        
    def __str__(self):
        out = f"{self.name} ({'dir' if self.type == 'dir' else f'file, size={self.size}'})\n"
        for entry in self.children:
            out += " "*2*self.level +f"↳ {entry}"
        return out 
    
    def get_level(self):
        if self.parent == None: return 0
        return self.parent.level + 1
    
    def goto(self, direction):
        if direction == "..": return self.parent
        elif direction == ".": return self
        elif direction == "/": 
            x = self
            while x.parent != None:
                x = x.parent
            return x
        else:
            for entry in self.children:
                if entry.name == direction:
                    return entry
        raise Exception(f"goto command failed with input: {direction}")
    
    def get_size(self):
        if self.type == "file" or self.size != 0: return self.size
        i = 0
        for entry in self.children:
            i += entry.get_size()
        self.size = i
        return i
    
    def get_subdirectories(self):
        a = []
        if self.type == "dir": a.append(self)
        for entry in self.children:
            if entry.type=="dir": a= a+entry.get_subdirectories()
        return a      
             
def init():
    data = []
    with open("input.txt", "r") as f:
        for lines in f:
            sublines = [x.strip() for x in lines.split(" ")]
            data.append(sublines)   
    N = Node("root", "dir", None)
    return data, N

def seven1(data, root):
    current_node = root
    i = -1
    while i < len(data)-1:
        i+=1
        if data[i][0] != "$": raise Exception(f"$ expected but not found in: {data[i]}") 
        if data[i][1] == "cd":
            current_node = current_node.goto(data[i][2])
        elif data[i][1] == "ls":
            while True:
                i+=1
                if i ==len(data): break
                if data[i][0] == "$":
                    i -= 1
                    break
                if data[i][0] == "dir":
                    Node(data[i][1], "dir", current_node)
                else:
                    Node(data[i][1], "file", current_node, int(data[i][0]))
        else:
            raise Exception(f"Error reading line: {data[i]}")
    a = 0
    for entry in root.get_subdirectories():
        if entry.get_size() <= 100000:
            a+=entry.get_size()
    print(f"{root}\n1) Sum of size of folders smaller than 100000: {a}")
    
def seven2(root):
    install_space = 70000000-root.get_size()-30000000
    temp=float("inf")               #always the biggest number
    saved_node = None
    
    for entry in root.get_subdirectories():
        y = entry.get_size()
        x = y + install_space       #space when deleting current iterated dir
        if x >= 0 and y < temp: 
            temp = y
            saved_node = entry
    
    print(f"2) The smallest directory to delete so that enough space is freed up is {saved_node.name} with a size of {temp}")
            
data, N = init()
seven1(data, N)
seven2(N)