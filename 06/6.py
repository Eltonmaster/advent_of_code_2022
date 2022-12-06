
def init():
    with open("input.txt", "r") as f:
        data = f.read().strip()
    return data

def marker_finder(string, amount):
    a = []
    for i in range(0, len(string)):
        if string[i] in a:
            a.append(string[i])
            temp = a.index(string[i])
            a = a[a.index(string[i])+1:]
            continue
        else:
            a.append(string[i])
        
        if len(a) < amount: continue
        return i+1

def six1(data):
    print(f"1) Position of marker: {marker_finder(data, 4)}")
   
def six2(data):
    print(f"2) Position of message marker: {marker_finder(data, 14)}") 
  
data = init()

six1(data)
six2(data)


#nznrnfrfntjfmvf wmzdfjlvtqnbhc prsg