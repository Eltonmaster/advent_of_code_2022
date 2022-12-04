import sys

def init():
    dic = {}
    j=1
    for i in "abcdefghijklmnopqrstuvwxyz":
        dic[i] = j
        j+=1
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dic[i] = j
        j+=1
    data= []
    with open("input.txt", "r") as f:
        for lines in f:
            data.append(lines.strip())
    return dic, data

def get_duplicate(dic, string1, string2):
    for part in string1:
        if part in string2:
            return dic[part]
    return -1

def find_common(s1, s2, s3):
    for entry1 in s1:
        for entry2 in s2:
            for entry3 in s3:
                if entry1==entry2==entry3:
                    return entry1
    

def three1(dic, data):
    x = 0
    for entry in data:
        left = entry[:int(len(entry)/2)]
        right = entry[int(len(entry)/2):]
        z = get_duplicate(dic, left, right)
        if z >-1:
            x+= get_duplicate(dic, left, right)
        else:
            raise Exception(f"Problem with case {entry}")
    print(f"1) Sum of priorities: {x}")
    
def three2(dic, data):
    x = 0
    for i in range(0, len(data)):
        if i % 3 == 0:
            x += dic[find_common(data[i],data[i+1],data[i+2])]
            
    print(f"2) Sum of group badge priorities: {x}")
            

dic, data = init()
three1(dic, data)
three2(dic, data)