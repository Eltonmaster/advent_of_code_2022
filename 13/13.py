from functools import cmp_to_key

def init():
    with open("input.txt") as f:
        return [lines.strip() for lines in f]


def pre_compare(arr1, arr2):
    length = max(len(arr1), len(arr2))
    for i in range(length):
        if len(arr1) != len(arr2):
            if len(arr1) < len(arr2):
                if i == len(arr1): return True
            if len(arr1) > len(arr2):
                if i == len(arr2): return False
        ret = compare(arr1[i], arr2[i])
        if ret: return True
        if ret == False: return False

def compare(x, y):
    if type(x) is int and type(y) is int:
        if x < y: return True
        if x > y: return False
        return None
    
    if type(x) is list and type(y) is int:
        return compare(x, [y])
    
    if type(x) is int and type(y) is list:
        return compare([x], y)
    
    if type(x) is list and type(y) is list:
        return pre_compare(x, y)
    return None

def wrap_compare(x,y):
    ret = pre_compare(x,y)
    if ret: return 1
    elif ret == False: return -1
    return 0

def pre_parse(inp):
    stack = []
    for i in inp:
        stack.append(i)
    return parse(stack)

def parse(stack):
    a = []
    num_str = ""
    while len(stack) > 0:
        char = stack.pop(0)
        if char == "[":
            if len(num_str) > 0:
                a.append(int(num_str))
                num_str = ""
            temp = parse(stack)
            a.append(temp)
        elif char == ",":
            if len(num_str) > 0:
                a.append(int(num_str))
                num_str = ""
            continue
        elif char == "]":
            if len(num_str) > 0:
                a.append(int(num_str))
                num_str = ""
            num_str = ""
            return a
        else:
            if len(num_str) > 0:
                if char.isdigit():
                    num_str += char
            num_str += char
    return a[0]
        
        
def thirteen1(data):
    sum = 0
    index = 0 
    for i in range(len(data)):
        if i % 3 == 0:
            index += 1
            a = pre_parse(data[i])
            b = pre_parse(data[i+1])     
            if pre_compare(a,b): sum += index
    print(f"1) Sum of correctly ordered indexes: {sum}")

def thirteen2(data):
    inputs = [[[2]], [[6]]]
    for i in range(len(data)):
        if i % 3 == 0:
            inputs.append(pre_parse(data[i]))
            inputs.append(pre_parse(data[i+1]))
    inputs.sort(key=cmp_to_key(wrap_compare))
    inputs.reverse()
    
    begin = inputs.index([[2]])+1
    end = inputs.index([[6]])+1

    print(f"2) Decoder key: {begin * end}")


thirteen1(init())
thirteen2(init())
