listador = range(1, 21)

for num  in listador:
    if num >9 and num <11:
        continue
    if num == 16:
        break
    
    print(num)