def init():
    data = []
    with open("input.txt", "r") as f:
        for lines in f:
            sublines = [int(x) for x in lines.strip()]
            data.append(sublines)
    return data

def vision_check(i, j, data):
    h = data[i][j]
    
    vis_left = True
    for x in range(0,j):  #test if visible from the left side
        if data[i][x] < h: continue
        vis_left = False
        break
    if vis_left: return True
        
    vis_top = True
    for x in range(0,i):  #test if visible from the top
        if data[x][j] < h: continue
        vis_top = False
        break
    if vis_top: return True

    vis_right = True
    for x in range(j+1,len(data[i])):  #test if visible from the right side
        if data[i][x] < h: continue
        vis_right = False
        break
    if vis_right: return True
    
    vis_bot = True
    for x in range(i+1,len(data)):  #test if visible from the bottom
        if data[x][j] < h: continue
        vis_bot = False
        break
    if vis_bot: return True#
    return False

def calculate_scenic_score(i, j, data):
    h = data[i][j]
    
    vis_left = 0
    for x in reversed(range(0,j)):  #get visible trees to the left
        vis_left+=1
        if data[i][x] < h: continue
        break
        
    vis_top = 0
    for x in reversed(range(0,i)):  #get visible trees to the top
        vis_top+=1
        if data[x][j] < h: continue
        break

    vis_right = 0
    for x in range(j+1,len(data[i])):  #get visible trees to the right
        vis_right+=1
        if data[i][x] < h: continue
        break
    
    vis_bot = 0
    for x in range(i+1,len(data)):  #get visible trees to the bottom
        vis_bot+=1
        if data[x][j] < h: continue
        break    
    return vis_left*vis_top*vis_right*vis_bot
            
def eight1(data):
    a = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if vision_check(i,j,data):
                a+=1
    print(f"1) Amount of hidden Trees: {a}")
    
def eight2(data):
    a = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            temp = calculate_scenic_score(i,j,data)
            if temp > a: a = temp
    print(f"2) Highest achievable scenic scode: {a}")       

data = init()
eight1(data)
eight2(data)
