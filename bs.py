import sys
import math

while True:
    a = []
    
    lines = int(input())
    for i in range(lines):
        line = input()
        print(line, file=sys.stderr)
        a.append(line)
        
    if a[0] == "ss_n: Unauthorized":
        numbers = a[1][1:].split(", ")
        s2 = numbers[-1]
        numbers.pop()
        numbers = list(map(int, numbers))
        repeat = int(s2.split("[")[1].split("]")[0])
        current = len(numbers)
        while current < repeat+1:
            numbers.append( (numbers[-1]+numbers[-2]) )
            current+=1;
            
        print(numbers, file=sys.stderr)
        answer0 = a[1].split("...")[1]
        answer1 = "[..." + ', '.join(str(e) for e in numbers[5:]) + "]" #answer0
        print(answer1, file=sys.stderr)
            
        print(numbers[-1])
        
    elif a[0] == "rs_n: Unauthorized":
        numbers = a[1][1:].split(", ")
        s2 = numbers[-1]
        numbers.pop()
        numbers = list(map(int, numbers))
        repeat = int(s2.split("[")[1].split("]")[0])
        current = len(numbers)
        diff = numbers[1] - numbers[0]
        while current < repeat+1:
            numbers.append( (numbers[-1]+diff) )
            current+=1;
            
        print(numbers[-1])
        
    else:
        print("shitty puzzle")
