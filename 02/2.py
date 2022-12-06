
def init(): 
    data = []
    with open("input.txt", "r") as f:
        for lines in f:
            data.append(lines)
    return data
            
def validate():
    jan_i = []
    jan_o = []
    s_out = ""
    with open("jan.txt", "r") as f:
        for line in f:
            jan_i.append(line)   
    with open("jan_output.txt", "r") as f:
        for line in f:
            jan_o.append(line)
    for i in range(0, len(jan_i)):
        score = calc_points_1(jan_i[i])
        if score != int(jan_o[i]):
            s_out += f"Difference in case {jan_i[i].strip()}. Got {jan_o[i].strip()} but expected {score}\n"
    with open("val.txt", "w") as f:
        f.write(s_out)

def calc_points_1(x):
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

def calc_points_2(x):
    #A=Rock B=Paper C=Scissors
    #Rock=1 Paper=2 Scissors=3
    #Win=6 Draw=3 Loss=0
    enemy, you = x.strip().split(" ") 
    
    if enemy == "A":
        if you == "Z":
            return 6+2
        if you == "Y":
            return 3+1
        if you == "X":
            return 0+3

    if enemy == "B":
        if you == "Z":
            return 6+3
        if you == "Y":
            return 3+2
        if you == "X":
            return 0+1
        
    if enemy == "C":
        if you == "Z":
            return 6+1
        if you == "Y":
            return 3+3
        if you == "X":
            return 0+2

    raise Exception (f"Match was not calculated correctly: {x}")

def two1(data):
    a = 0
    for entry in data:
        a+= calc_points_1(entry)
    print(f"1) Points: {a}")
    
def two2(data):
    a = 0
    for entry in data:
        a+= calc_points_2(entry)
    print(f"2) Points: {a}")
    

data = init()
# two1(data)
# two2(data)
validate()