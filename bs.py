import sys
import math

while True:
    a = []
    y = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']  
    
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
        
    elif a[0] == "ss_f: Unauthorized" or a[0] == "rs_f: Unauthorized":
        ab = "abcdefghijklmnopqrstuvwxyz"
        for c in a[1]:
            if c.islower():
                # print( len(a[1]) - a[1].find(c) )
                print( ab.find(c) )

    elif a[0] == "gs_m: Unauthorized":
        a[1] = a[1].split(' ')[2]
        print(y[int(a[1])-1])

    elif a[0] == "ss_m: Unauthorized":
        print(y.index(a[1])+1)

    elif a[0] == "ss_con: Unauthorized":
        a[1] = a[1].split('...')
        it = 0
        while a[1][it][1] == 'G':
            it+=1
        if a[1][it][2] != 'O':
            print(a[1][it][2])
        else:
            print('O')

    elif a[0] == "ss_colv: Unauthorized":
        # a[1] = a[1].replace('-','+')
        # a[1] = a[1].replace('G-','G+')
        print(a[1])

    else:
        print("shitty puzzle")
