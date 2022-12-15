class Node:
    def __init__(self, height, value=float("inf")):
        self.value = value
        self.height = dic[height]
        self.pred = None
        self.edges = []
        
    def add_edge(self, x, dist):
        temp = {"node":x, "distance": dist}
        if temp not in self.edges: self.edges.append(temp)
        
    def add_neighbour(self, x, dist):
        temp = {"node":x, "distance": dist}
        if temp not in self.edges: self.edges.append(temp)
        if x.reachable(self):
            temp2 = {"node":self, "distance": dist}
            if temp2 not in x.edges: x.edges.append(temp2)
    
    def check_edges(self):
        for entry in self.edges:
            if entry["node"].value > self.value + entry["distance"]:
                entry["node"].value = self.value + entry["distance"]
                entry["node"].pred = self
    
    def __str__(self):
        return str(self.height)
    
    def reachable(self, x):
        return x.height <= self.height+1
        
        
def init():
    with open("input.txt") as f:
        data_in = [lines.strip() for lines in f]
        data = []
        start_positions = []
        for i in range(len(data_in)):
            temp = []
            for j in range(len(data_in[i])):
                if data_in[i][j] == "S":
                    n = Node("a") 
                    start_positions.insert(0, n)
                elif data_in[i][j] == "E":
                    n = Node("z")
                    end_node = n
                elif data_in[i][j] == "a":
                    n = Node("a")
                    start_positions.append(n)
                else:
                    n = Node(data_in[i][j])
                temp.append(n)
            data.append(temp)
            
    node_list = []        
    for i in range(len(data)):
        for j in range(len(data[i])):
            current = data[i][j]
            node_list.append(current)
            if i == 0 and j == 0:   #upper left
                if current.reachable(data[i][j+1]): current.add_neighbour(data[i][j+1], 1)
                if current.reachable(data[i+1][j]): current.add_neighbour(data[i+1][j], 1)            
            elif i == 0 and j == len(data[i])-1:    #upper right
                if current.reachable(data[i][j-1]): current.add_neighbour(data[i][j-1],1)
                if current.reachable(data[i+1][j]): current.add_neighbour(data[i+1][j],1)
            elif i == 0:    #upper row bot not first nor last
                if current.reachable(data[i][j-1]): current.add_neighbour(data[i][j-1],1)
                if current.reachable(data[i+1][j]): current.add_neighbour(data[i+1][j],1)
                if current.reachable(data[i][j+1]): current.add_neighbour(data[i][j+1],1)   
            elif i == len(data)-1 and j == 0:   #lower left
                if current.reachable(data[i][j+1]): current.add_neighbour(data[i][j+1],1)  
            elif i == len(data)-1 and j == len(data[i])-1:   #lower right
                if current.reachable(data[i][j-1]): current.add_neighbour(data[i][j-1],1)  
            elif i == len(data)-1:   #lower row
                if current.reachable(data[i][j+1]): current.add_neighbour(data[i][j+1],1)  
                if current.reachable(data[i][j-1]): current.add_neighbour(data[i][j-1],1) 
                #don't need to check upwards as this connection was already set in previous i run
            elif j == 0:    #left side
                if current.reachable(data[i+1][j]): current.add_neighbour(data[i+1][j],1)
                if current.reachable(data[i][j+1]): current.add_neighbour(data[i][j+1],1)  
                #don't need to check upwards as this connection was already set in previous i run    
            elif j == len(data[i])-1:    #right side
                if current.reachable(data[i+1][j]): current.add_neighbour(data[i+1][j],1)
                if current.reachable(data[i][j-1]): current.add_neighbour(data[i][j-1],1)  
                #don't need to check upwards as this connection was already set in previous i run  
            else:
                if current.reachable(data[i][j-1]): current.add_neighbour(data[i][j-1],1)
                if current.reachable(data[i+1][j]): current.add_neighbour(data[i+1][j],1)
                if current.reachable(data[i-1][j]): current.add_neighbour(data[i-1][j],1)
                if current.reachable(data[i][j+1]): current.add_neighbour(data[i][j+1],1)
    
    return data, node_list, start_positions, end_node

def get_steps(node_list, end_node, start_node):
    local_list = node_list.copy()
    local_list.insert(0, start_node)
    count = 0
    while count < len(node_list):
        count+=1
        local_list.sort(key=lambda x:x.value)
        local_list[0].check_edges()
        local_list.pop(0)
        
    i = 0  
    end = end_node
    while end.pred != None:
        i+=1
        end= end.pred        
    return i-1

    

def twelve1(node_list, start_positions, end_node):
    n = Node("a", value=0)      #node connected one way to the real starting node
    n.add_edge(start_positions[0], 0)
    steps = get_steps(node_list, end_node, n)  
    print("1) Required Steps: "+str(steps))
            
def twelve2(node_list, start_positions, end_node):
    n = Node("a", value=0)      #node connected one way to all the nodes with height 0
    for entry in start_positions:
        n.add_edge(entry, 0)
    steps = get_steps(node_list, end_node, n)  
    print("2) Least Steps: "+str(steps))

            
    
alphabet = "abcdefghijklmnopqrstuvwxyz"
dic = {}
for i in alphabet:
    dic[i] = alphabet.index(i)


data, node_list, start_positions, end_node = init()
twelve1(node_list, start_positions, end_node)    
data, node_list, start_positions, end_node = init()
twelve2(node_list, start_positions, end_node)   


    
    

        