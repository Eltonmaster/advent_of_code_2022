def init():
    #x is distance to right
    #is distance down
    challenge_map = [["." for i in range(1000)] for j in range(1000)]
    data = [lines.strip() for lines in open("input.txt").readlines()]
    rock_data = []
    for entry in data:
        rock_parts = entry.split(" -> ")
        for i in range(len(rock_parts)):
            rock_parts[i] = (int(rock_parts[i].split(",")[0]),int(rock_parts[i].split(",")[1]))
        rock_data.append(rock_parts)
    
    lowest_row = 0
    leftest_column = float("inf")
    rightest_column = 0
 
    for entry in rock_data:
        for i in range(len(entry)):
            if entry[i][1] > lowest_row: lowest_row = entry[i][1]
            if entry[i][0] > rightest_column: rightest_column = entry[i][0]
            if entry[i][0] < leftest_column: leftest_column = entry[i][0]
            if i == len(entry)-1: continue
            first = entry[i]
            next = entry[i+1]
        
            if first[0] == next[0]:
                if first[1] > next[1]:
                    temp = next
                    next = first
                    first = temp
                for i in range(first[1], next[1]+1):
                    y = i
                    x = first[0]
                    challenge_map[y][x] = "#"
                continue
            
            if first[0] > next[0]:
                temp = next
                next = first
                first = temp  
                          
            for i in range(first[0], next[0]+1):
                y = first[1]
                x = i
                challenge_map[y][x] = "#"
    
    lowest_row += 4
    leftest_column -= 10
    rightest_column += 10
    challenge_map = challenge_map[:lowest_row+1]
    #for i in range(len(challenge_map)):
    #    challenge_map[i] = challenge_map[i][leftest_column:rightest_column]
    
    #sand_source = 500-leftest_column
    sand_source = 500
    
    #draw_map(challenge_map)
    
    return challenge_map, sand_source

def draw_map(c_map):
    out_s = ""
    for entry in c_map:
        for char in entry:
            out_s += char
        out_s += "\n"
    print(f"{out_s}\n")

def simulate_fall(challenge_map, sand_pos):
    if sand_pos[1]+2 == len(challenge_map): return False
    if challenge_map[0][sand_pos[0]] == "0": return False
    x = sand_pos[0]
    y = sand_pos[1]
    below_left = "blocked" if challenge_map[y+1][x-1] in ["#","0"] else "free"
    below = "blocked" if challenge_map[y+1][x] in ["#","0"] else "free"
    below_right = "blocked" if challenge_map[y+1][x+1] in ["#","0"] else "free"
        
    if below == "free": return simulate_fall(challenge_map, [x, y+1])  
    
    if below_left == "blocked" and below == "blocked" and below_right == "blocked":
        challenge_map[y][x] = "0"
        return True
    
    if below == "blocked" and below_left == "free": return simulate_fall(challenge_map, [x-1, y+1])
    
    if below == "blocked" and below_right == "free": return simulate_fall(challenge_map, [x+1, y+1])
    


def fourteen1(challenge_map, sand_source):
    counter = 0
    while True:
        if simulate_fall(challenge_map, [sand_source, 0]):
            #draw_map(challenge_map)
            counter += 1
        else:
            print(f"1) Steps until sand falls into the void: {counter}")
            break
    return counter
        
def fourteen2(challenge_map, sand_source, counter):
    for i in range(len(challenge_map[-3])):
        challenge_map[-3][i] = "#"
    #draw_map(challenge_map)
    while True:
        if simulate_fall(challenge_map, [sand_source, 0]):
            #draw_map(challenge_map)
            counter += 1
        else:
            print(f"2) Steps until all sand settles and the input is blocked: {counter}")
            #draw_map(challenge_map)
            break    
    


challenge_map, sand_source = init()
x = fourteen1(challenge_map, sand_source)
fourteen2(challenge_map, sand_source, x)