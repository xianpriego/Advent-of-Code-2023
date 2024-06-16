
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

acum = 0
for line in lines:

    foundN1 = False
    foundN2 = False
    length = len(line)
    p1 = 0
    p2 = len(line) - 1
    n1 = line[p1]
    n2 = line[p2]

    if n1.isdigit() :
        foundN1 = True
    if n2.isdigit() :
        foundN2 = True
        
    while not foundN1 or not foundN2:
        if not foundN1:
            p1 += 1
            n1 = line[p1]
            foundN1 = n1.isdigit()
        if not foundN2:
            p2 -= 1
            n2 = line[p2]
            foundN2 = n2.isdigit()
    
    n = int(n1 + n2)
    acum += n

print(acum)

