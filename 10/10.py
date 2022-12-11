def init():
    with open("input.txt") as f:
        return [lines.rstrip().split(" ") for lines in f]

def ten1(data):
    x = 1
    cycle = 1
    sig_str_list = []
    for i in range(0, len(data)):
        if cycle % 40 == 20: sig_str_list.append(cycle*x)
        
        if data[i][0] == "noop":
            cycle+=1
        
        elif data[i][0] == "addx":
            cycle+=1
            if cycle % 40 == 20: sig_str_list.append(cycle*x)
            cycle+=1
            x+= int(data[i][1])
    
    print(f"1) Sum of signalstrength values: {sum(sig_str_list)}")
    
def draw(x, pos, display):
    if x in range(pos-1, pos+2):
        display.append("#")
    else: display.append(".")

def ten2(data):
    x = 1
    cycle = 1
    crt_position = 0
    display = []
    for i in range(0, len(data)):
        draw(x, crt_position % 40, display)
        
        if data[i][0] == "noop":
            cycle+=1
            crt_position+=1
        
        elif data[i][0] == "addx":
            cycle+=1
            crt_position+=1
            draw(x, crt_position % 40, display)
            cycle+=1
            crt_position+=1
            x+= int(data[i][1])
            
    out = ""
    for i in range(0, len(display)):
        if i % 40 == 0: out+="\n"
        out+=display[i]
    
    print(f"2) Display: {out}")


ten1(init())
ten2(init())