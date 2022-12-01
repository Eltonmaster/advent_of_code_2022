
a = [0]
with open("input.txt", "r") as f:
    for lines in f:
        if lines == "\n":
            a.append(0)
            continue
        if a[len(a)-1] == 0:
            a[len(a)-1] = int(lines.strip())
        else:
            a[len(a)-1] += int(lines.strip())
            
a.sort()
print(f"1) Most Calories: {a[-1]}")
print(f"2) Calories of top 3: {sum(a[-3:])}")
            