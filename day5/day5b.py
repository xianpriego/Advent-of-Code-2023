from typing import List, Dict
import os

def read_lines(filename: str) -> tuple[List[str], Dict]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        maps = {}
        
        for line in lines:
            line = line.strip()

            if line.startswith("seeds:"):
                seed_ranges = list(map(int, line.replace("seeds:", "").strip().split()))
                
            elif "map:" in line:
                current_map = line.replace(" map:", "").strip()
                maps[current_map] = []
            elif line:
                trio = list(map(int, line.split()))
                maps[current_map].append(trio)

        map_list = []
        for m in maps:
            aux_map = {}
            for l in maps[m]:
                aux_map[(l[0], l[1], l[2])] = l[0] - l[1]
            map_list.append(aux_map)


    return seed_ranges, map_list

def compute_seed_ranges(seeds: List[str]) -> List[tuple]:
    ranges = []
    for i in range(0,len(seeds),2):
        ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))
    return ranges
    
def process_lines(seed_ranges: List[str], maps: List) -> List:
    initial_ranges = compute_seed_ranges(seed_ranges)
    solution = []
    for range in initial_ranges:
        ranges_to_process = [range]
        following = []
        for map in maps:
            while ranges_to_process:
                left, right = ranges_to_process.pop()
                count = 0
                for dest, source, range_size in map:
                    count += 1
                    offset = dest - source
                    source_left, source_right = (source, source + range_size - 1)
                    # Caso en el que el rango está incluido:
                    if (left >= source_left and right <= source_right):
                        transformed_range = (left + offset, right + offset)
                        following.append(transformed_range)
                        break
                    # Caso en el que sobra por la izquierda: 
                    elif (left < source_left and source_left <= right <= source_right):
                        transformed_range = (source_left + offset, right + offset)
                        ranges_to_process.append((left, source_left - 1))
                        following.append(transformed_range)
                        break
                    # Caso en el que sobra por la derecha
                    elif (right > source_right and source_left <= left <= source_right):
                        transformed_range = (left + offset, source_right + offset)
                        ranges_to_process.append((source_right + 1, right))
                        following.append(transformed_range)
                        break
                    # Caso en que sobresale por ambos lados
                    elif (left < source_left and right > source_right):
                        transformed_range = (source_left + offset, source_right + offset)
                        ranges_to_process.append((left, source_left - 1))
                        ranges_to_process.append((source_right + 1, right))
                        following.append(transformed_range)
                        break
                    else:  # No coincide con nada
                        if count == len(map): # Si estamos en el último rango del map, no va a coincidir con nada, por lo que se pasa para delante                    
                            following.append((left, right))
            
            ranges_to_process = following
            following = []
        for range in ranges_to_process:
            solution.append(range)
    # Obtenemos el mínimo de las locations
    min = float('inf')
    for range in solution:
        if range[0] < min:
            min  = range[0]

    return min
    
if __name__ == '__main__':
    seed_ranges, maps = read_lines(os.path.join('day5', 'input.txt'))
    min_location = process_lines(seed_ranges, maps)
    print(min_location)

