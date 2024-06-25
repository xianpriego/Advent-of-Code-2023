from typing import List, Dict

def read_lines(filename: str) -> tuple[List[str], Dict]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        time = int(lines[0].split(':')[1].replace(" ", ""))
        distance = int(lines[1].split(':')[1].replace(" ", ""))
        
    
    return (time, distance)

def calculate_options(race: tuple[int, int]) -> int:
    time, record = race

    n_options = 0
    for i in range(time):
        pulse_time = i
        speed = pulse_time
        travelling_time = time - pulse_time
        traveled_dist = travelling_time * speed
        if traveled_dist > record:
            n_options += 1
    
    return n_options
               

if __name__ == '__main__':
    race = read_lines('input.txt')
    print(race)
    options = calculate_options(race)
    print(options)