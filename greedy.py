from functools import reduce


vstup = open('profit.txt')
vstupy = []
for line in vstup:
    vstupy.append([int(x) for x in line.strip().split()])
    
maxden = list(reduce(lambda x,y: x if x > y else y, vstupy))[0]
vstupy.sort(key=lambda x: x[1])
vstupy = vstupy[-1::-1]
vystup = [[] for i in range(maxden)]


for profit in vstupy:
    kedy_spravim = profit[0]-1
    while kedy_spravim >=0:
        if len(vystup[kedy_spravim])==0:
            vystup[kedy_spravim].append(profit)
            break
        else: 
            kedy_spravim-=1
    
vystup2 = []
for den in vystup:
    if len(den)!=0:
        vystup2.append(den[0])
    
print(vystup2)
print(maxden - len(vystup2), "dni chillujem")


