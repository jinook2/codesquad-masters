import random

def num_gen():
    numbers = list(range(1, 9))*3
    random.shuffle(numbers)
    return numbers[0:18]

def num_arrange(input_list):
    arranged_list=[]
    arranged_list.append(input_list[0:6])
    arranged_list.append(input_list[6:12])
    arranged_list.append(input_list[12:18])
    return arranged_list

def doublelist_displayer(input_list):
    for i in input_list:
        for j in i:
            print(j,end=" ")
        print()

notarranged_numlist=num_gen()
numlist=num_arrange(notarranged_numlist)
player_list=[["x"]*6]*3

doublelist_displayer(numlist)
doublelist_displayer(player_list)