num = [2,2,3,4,5,5]

uniques = []

for number in num:
    if number not in uniques:
        uniques.append(number)
        print(uniques)
