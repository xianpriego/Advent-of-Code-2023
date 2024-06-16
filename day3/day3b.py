from typing import List, Tuple, Dict

def read_lines(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def initialize_gears(n: int, m: int) -> Dict[Tuple[int, int], Tuple[int, int]]:
    gears = {}
    for i in range(n):
        for j in range(m):
            gears[(i, j)] = (1, 0)
    return gears

def gear_adjacent(row: int, left: int, right: int, lines: List[str], gears: Dict[Tuple[int, int], Tuple[int, int]], n: int, m: int) -> None:
    number = int(lines[row][left + 1:right])

    if left < 0:
        left = 0
    if right >= m:
        right = m - 1

    c1 = lines[row][left]
    c2 = lines[row][right]
    if c1 == '*':
        gears[(row, left)] = (gears[(row, left)][0] * number, gears[(row, left)][1] + 1)
    if c2 == '*':
        gears[(row, right)] = (gears[(row, right)][0] * number, gears[(row, right)][1] + 1)

    if row == 0:
        for j in range(left, right + 1):
            c = lines[row + 1][j]
            if c == '*':
                gears[(row + 1, j)] = (gears[(row + 1, j)][0] * number, gears[(row + 1, j)][1] + 1)
    elif row == n - 1:
        for j in range(left, right + 1):
            c = lines[row - 1][j]
            if c == '*':
                gears[(row - 1, j)] = (gears[(row - 1, j)][0] * number, gears[(row - 1, j)][1] + 1)
    else:
        for j in range(left, right + 1):
            c1 = lines[row - 1][j]
            c2 = lines[row + 1][j]
            if c1 == '*':
                gears[(row - 1, j)] = (gears[(row - 1, j)][0] * number, gears[(row - 1, j)][1] + 1)
            if c2 == '*':
                gears[(row + 1, j)] = (gears[(row + 1, j)][0] * number, gears[(row + 1, j)][1] + 1)

def process_lines(lines: List[str], gears: Dict[Tuple[int, int], Tuple[int, int]], n: int, m: int) -> None:
    for i in range(n):
        j = 0
        while j < m:
            if lines[i][j].isdigit():
                j_aux = j + 1
                while j_aux < m and lines[i][j_aux].isdigit():
                    j_aux += 1
                gear_adjacent(i, j - 1, j_aux, lines, gears, n, m)
                j = j_aux
            else:
                j += 1

def calculate_acum(gears: Dict[Tuple[int, int], Tuple[int, int]]) -> int:
    acum = 0
    for value in gears.values():
        if value[1] == 2:
            acum += value[0]
    return acum

if __name__ == '__main__':
    lines = read_lines('input.txt')
    n = len(lines)
    m = len(lines[0])
    gears = initialize_gears(n, m)
    process_lines(lines, gears, n, m)
    acum = calculate_acum(gears)
    print(acum)
