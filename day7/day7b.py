from typing import List
from enum import Enum
import heapq
from operator import itemgetter

card_order = {
    'J' : 0,
    '2' : 1,
    '3' : 2,
    '4' : 3,
    '5' : 4,
    '6' : 5,
    '7' : 6,
    '8' : 7,
    '9' : 8,
    'T' : 9,
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
    joker = False
    for card in hand:
        if card == 'J':
            joker = True
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
            if joker:
                return category.FIVE_OF_A_KIND
            else:
                return category.FOUR_OF_A_KIND
        case [3,2]:
            if joker:
                return category.FIVE_OF_A_KIND
            else:
                return category.FULL_HOUSE
        case [3, 1, 1]:
            if joker:
                return category.FOUR_OF_A_KIND
            else:
                return category.THREE_OF_A_KIND
        case [2, 2, 1]:
            if joker and counts['J'] == 1:
                return category.FULL_HOUSE
            elif joker:
                return category.FOUR_OF_A_KIND
            else:
                return category.TWO_PAIR
        case [2, 1, 1, 1]:
            if joker:
                return category.THREE_OF_A_KIND
            else:
                return category.ONE_PAIR
        case _:
            if joker:
                return category.ONE_PAIR
            else:
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