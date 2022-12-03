
def init(): 
    data = []
    with open("input.txt", "r") as f:
        for lines in f:
            data.append(lines)
    return data
            
def calc_points(x):
    #A=Rock B=Paper C=Scissors
    #Rock=1 Paper=2 Scissors=3
    #Win=6 Draw=3 Loss=0
    x = x.replace("X","A").replace("Y","B").replace("Z","C")
    enemy, you = x.strip().split(" ") 
    if enemy == you:
        if enemy == "A": return 3+1
        elif enemy == "B": return 3+2
        else: return 3+3 
    if enemy == "A" and you == "B": return 6+2
    if enemy == "A" and you == "C": return 0+3
    if enemy == "B" and you == "A": return 0+1
    if enemy == "B" and you == "C": return 6+3
    if enemy == "C" and you == "A": return 6+1
    if enemy == "C" and you == "B": return 0+2
    raise Exception (f"Match was not calculated correctly: {x}")

def two1(data):
    a = 0
    for entry in data:
        a+= calc_points(entry)
    print(f"1) Points: {a}")
    
    

data = init()
two1(data)

