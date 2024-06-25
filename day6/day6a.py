from typing import List, Dict

def read_lines(filename: str) -> tuple[List[str], Dict]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        times = lines[0].split(':')[1].split()
        distances = lines[1].split(':')[1].split()

        n_races = len(times)
        races = []
        for i in range(n_races):
            races.append((int(times[i]), int(distances[i])))
    
    return races

def calculate_options(races: List) -> int:
    multiplier = 1
    for time, record in races:
        n_options = 0
        for i in range(time):
            pulse_time = i
            speed = pulse_time
            travelling_time = time - pulse_time
            traveled_dist = travelling_time * speed
            if traveled_dist > record:
                n_options += 1
        
        multiplier *= n_options
    
    return multiplier
               

if __name__ == '__main__':
    races = read_lines('input.txt')
    options = calculate_options(races)
    print(options)