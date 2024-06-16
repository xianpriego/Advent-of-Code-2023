from typing import List

def read_lines(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def is_adjacent(row: int, left: int, right: int, lines: List[str], n: int, m: int) -> bool:
    if left < 0:
        left = 0
    if right >= m:
        right = m - 1

    c1 = lines[row][left]
    c2 = lines[row][right]
    if (c1 != '.' and not c1.isdigit()) or (c2 != '.' and not c2.isdigit()):
        return True

    if row == 0:
        check = lines[row + 1][left:right + 1]
        for c in check:
            if c != '.' and not c.isdigit():
                return True
    elif row == n - 1:
        check = lines[row - 1][left:right + 1]
        for c in check:
            if c != '.' and not c.isdigit():
                return True
    else:
        for j in range(left, right + 1):
            c1 = lines[row - 1][j]
            c2 = lines[row + 1][j]
            if (c1 != '.' and not c1.isdigit()) or (c2 != '.' and not c2.isdigit()):
                return True
    return False

def process_lines(lines: List[str]) -> int:
    n = len(lines)
    m = len(lines[0])
    acum = 0

    for i in range(n):
        j = 0
        while j < m:
            if lines[i][j].isdigit():
                j_aux = j + 1
                while j_aux < m and lines[i][j_aux].isdigit():
                    j_aux += 1
                if is_adjacent(i, j - 1, j_aux, lines, n, m):
                    number = int(lines[i][j:j_aux])
                    acum += number
                j = j_aux
            else:
                j += 1

    return acum

if __name__ == '__main__':
    lines = read_lines('input.txt')
    acum = process_lines(lines)
    print(acum)
