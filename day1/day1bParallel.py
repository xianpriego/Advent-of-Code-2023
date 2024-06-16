import multiprocessing
import time

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]


def process_line(line):     
    
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    TO_DIGITS= {'one': '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five': '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    windows = [2,3,4]

    foundN1 = False
    foundN2 = False
    p1 = 0
    p2 = len(line) - 1
    n1 = line[p1]
    n2 = line[p2]
    
    for i in windows :
        subString1 = line[p1:p1 + i + 1]
        subString2 = line[p2 - i:p2 + 1]
        if not foundN1 and subString1 in digits :
            n1 = TO_DIGITS[subString1]
            foundN1 = True
        if not foundN2 and subString2 in digits :
            n2 = TO_DIGITS[subString2]
            foundN2 = True
        if foundN1 and foundN2:
            break
        
    if n1.isdigit() :
        foundN1 = True
    if n2.isdigit() :
        foundN2 = True
        
    while not foundN1 or not foundN2:
        if not foundN1:
            p1 += 1
            n1 = line[p1]
            foundN1 = n1.isdigit()
            if not foundN1 :
                for i in windows :
                    subString1 = line[p1:p1 + i + 1]
                    if not foundN1 and subString1 in digits :
                        n1 = TO_DIGITS[subString1]
                        foundN1 = True
                        break
        if not foundN2:
            p2 -= 1
            n2 = line[p2]
            foundN2 = n2.isdigit()
            if not foundN2 : 
                for i in windows :
                    subString2 = line[p2 - i:p2 + 1]
                    if not foundN2 and subString2 in digits :
                        n2 = TO_DIGITS[subString2]
                        foundN2 = True
                        break
        
    n = int(n1 + n2)
    return n


if __name__ == '__main__':
   
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    start = time.time()

    pool = multiprocessing.Pool()

    results = pool.map(process_line, lines)

    pool.close()
    pool.join()

    acum = sum(results)

    end = time.time()

    print(end - start)