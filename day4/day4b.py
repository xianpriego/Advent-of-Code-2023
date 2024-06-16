from typing import List, Dict

def read_lines(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return [line.strip().split(':')[1].split('|') for line in file]
    
# index: índice de la carta (CardId - 1)
def number_of_copies(index: int, lines: List[str], num_of_winners: Dict) -> int:
    candidates = lines[index][0].split()
    winners =  lines[index][1].split()
    
    if num_of_winners[index] != -1:
        return num_of_winners[index]
    else:
        count = 0
        for i in candidates:
            if i in winners:
                count += 1
        #Base case:
        if count == 0:
            return 0
        #Recursive case:
        else:
            acum = count 
            for i in range(index+1, index+count+1):
                acum += number_of_copies(i, lines, num_of_winners)
            num_of_winners[index] = acum
            return acum

def process_lines(lines: List[str], num_of_winners: Dict) -> int:
    count = len(lines)
    for card in range(count):
       count += number_of_copies(card, lines, num_of_winners)
    return count

def initialize(n: int) -> Dict:
    num_of_winners = {}
    for i in range(n):
        num_of_winners[i] = -1
    return num_of_winners

if __name__ == '__main__':
    lines = read_lines('input.txt')
    num_of_winners = initialize(len(lines))
    acum = process_lines(lines, num_of_winners)
    print(acum)