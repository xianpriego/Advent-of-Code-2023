from typing import List

def read_lines(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return [line.strip().split(':')[1].split('|') for line in file]
    
def process_lines(lines: List[str]) -> int:
    acum = 0
    for line in lines:
        count = 0
        candidates = line[0].split()
        winners = line[1].split()
        for i in candidates:
            if i in winners:
                count += 1
        if count != 0:
            card_points = 2**(count-1)
            acum += card_points
    return acum

if __name__ == '__main__':
    lines = read_lines('input.txt')
    acum = process_lines(lines)
    print(acum)