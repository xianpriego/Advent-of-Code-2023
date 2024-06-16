with open('input.txt', 'r') as file:
    lines = [line.strip().split(':')[1].split(';') for line in file]


power_acum = 0
for line in lines: 
    maxQuant={}
    maxQuant['green'] = 0
    maxQuant['blue'] = 0
    maxQuant['red'] = 0

    for subset in line:
        elements = subset.split(',')
        for element in elements:
            parts = element.strip().split(' ')
            color = parts[1]
            quantity = int(parts[0])
            if quantity > maxQuant[color]:
                maxQuant[color] = quantity
    
    power = maxQuant['blue'] * maxQuant['green'] * maxQuant['red']
    power_acum += power
    

print(power_acum)