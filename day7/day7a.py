from typing import List
from enum import Enum
import heapq
from operator import itemgetter

card_order = {
    '2' : 0,
    '3' : 1,
    '4' : 2,
    '5' : 3,
    '6' : 4,
    '7' : 5,
    '8' : 6,
    '9' : 7,
    'T' : 8,
    'J' : 9,
    'Q' : 10,
    'K' : 11,
    'A' : 12
}

class category(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    
def hand_to_values(hand: str):
    return [card_order[card] for card in hand]


def read_lines(filename: str) -> List[tuple]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        hands = []
        for line in lines:
            line = line.split()
            hands.append((line[0], int(line[1])))
        return hands
    
def categorize(hand):

    counts = {}
    
    for card in hand:
        counts[card] = 0

    for card in hand:
        counts[card] += 1

    shape = []

    for card in counts:
        shape.append(counts[card])

    shape.sort(reverse=True)

    match shape:
        case [5]:
            return category.FIVE_OF_A_KIND
        case [4, 1]:
            return category.FOUR_OF_A_KIND
        case [3,2]:
            return category.FULL_HOUSE
        case [3, 1, 1]:
            return category.THREE_OF_A_KIND
        case [2, 2, 1]:
            return category.TWO_PAIR
        case [2, 1, 1, 1]:
            return category.ONE_PAIR
        case _:
            return category.HIGH_CARD

def total_winnings(hands: List) -> int:
    lst = []
    for hand, score in hands:
        ctgry = categorize(hand)
        card_values = hand_to_values(hand)
        lst.append((ctgry.value, card_values, score))
    
    sorted_lst = sorted(lst, key=itemgetter(0,1))
    winnings = 0
    for i in range(len(sorted_lst)):
        winnings += (i + 1) * sorted_lst[i][2]
    return winnings

if __name__ == '__main__':
    hands = read_lines('input.txt')
    winnings = total_winnings(hands)
    print(winnings)