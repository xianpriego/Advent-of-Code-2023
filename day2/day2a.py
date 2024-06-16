with open('input.txt', 'r') as file:
    lines = [line.strip().split(':')[1].split(';') for line in file]

CAPACITY = {'red' : 12, 'green' : 13, 'blue' : 14}
acum = 0
id = 1
for line in lines: 
    acum += id
    for subset in line:
        exit_second_loop = False
        elements = subset.split(',')
        for element in elements:
            parts = element.strip().split(' ')
            color = parts[1]
            quantity = int(parts[0])
            if quantity > CAPACITY[color]:
                acum -= id
                exit_second_loop = True
                break
        if exit_second_loop:
            break
    id += 1

print(acum)