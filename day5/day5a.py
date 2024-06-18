from typing import List, Dict

def read_lines(filename: str) -> tuple[List[str], Dict]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        seeds = []
        maps = {}
        
        for line in lines:
            line = line.strip()

            if line.startswith("seeds:"):
                seeds = list(map(int, line.replace("seeds:", "").strip().split()))
            elif "map:" in line:
                current_map = line.replace(" map:", "").strip()
                maps[current_map] = []
            elif line:
                trio = list(map(int, line.split()))
                maps[current_map].append(trio)

    return seeds, maps

def converting_to(origin: int, map: Dict) -> int:
    destination = origin
    for key in map:
        if origin in range(key[1], key[1] + key[2]):
            destination = origin + map[key]
    return destination


def process_lines(seeds: List[str], maps: Dict) -> List:
    map_list = []
    for map in maps:
        aux_map = {}
        for l in maps[map]:
            aux_map[(l[0], l[1], l[2])] = l[0] - l[1]
        map_list.append(aux_map)
    
    n = len(map_list)
    min = float('inf')
    for seed in seeds:
        aux = int(seed)
        for i in range(n):
            aux = converting_to(aux, map_list[i])
            if i == n-1 and aux < min:
                min = aux
    return min
    
if __name__ == '__main__':
    seeds, maps = read_lines('input.txt')
    min_location = process_lines(seeds, maps)
    print(min_location)
