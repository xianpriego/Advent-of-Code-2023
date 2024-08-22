from typing import List


def read_lines(filename: str) -> List[tuple]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        histories = [list(map(int,line.strip().split(" "))) for line in lines]
        return histories
    
def compute_diffs(list: List) -> tuple:
    all_zeros = True
    diffs = []
    for i in range(len(list)-1):
        diff = list[i+1] - list[i]
        diffs.append(diff)
        if diff != 0:
            all_zeros = False
    return diffs, all_zeros      
    
def prediction(history: List) -> int:
    all_zeros = False
    stack = [history[0]]
    aux = history
    while not all_zeros:
        aux, all_zeros = compute_diffs(aux)
        stack.append(aux[0])

    value = stack.pop()
    while stack:
        value = stack.pop() - value

    return value

    
def sum_predictions(histories: List[list]) -> int:
    total_sum = 0
    for hist in histories:
        total_sum += prediction(hist)
    return total_sum





if __name__ == '__main__':
    histories = read_lines('input.txt')
    print(sum_predictions(histories))
    
    
