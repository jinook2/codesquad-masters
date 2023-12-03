import random
import copy

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

def x_counter(input_list):
    count=0
    for i in input_list:
        count=count+i.count("x")
    return count

def finish_teller(input_list):
    input_list=[i for j in input_list for i in j]
    while (" " in input_list):
        input_list.remove(" ")
    return len(input_list)==len(set(input_list))

notarranged_numlist=num_gen()
numlist=num_arrange(notarranged_numlist)
player_list=[["x"]*6,["x"]*6,["x"]*6]

i=0
while (finish_teller(numlist) !=True):
    displayed_list=copy.deepcopy(player_list)
    doublelist_displayer(displayed_list)
    print()
    i=i+1
    print("<시도 {}, 남은 카드: {}> 좌표를 두 번 입력하세요".format(i,x_counter(player_list)))
    input1=input("입력 1? ").strip("()").split(",")
    input1=[int(input1[0])-1,int(input1[1])-1]
    input2=input("입력 2? ").strip("()").split(",")
    input2=[int(input2[0])-1,int(input2[1])-1]

    # print(displayed_list)
    displayed_list[input1[0]][input1[1]]=numlist[input1[0]][input1[1]]
    displayed_list[input2[0]][input2[1]]=numlist[input2[0]][input2[1]]
    # print(displayed_list)
    doublelist_displayer(displayed_list)

    if (numlist[input1[0]][input1[1]]==numlist[input2[0]][input2[1]]):
        player_list[input1[0]][input1[1]]=" "
        player_list[input2[0]][input2[1]]=" "
        numlist[input1[0]][input1[1]]=" "
        numlist[input2[0]][input2[1]]=" "        

    finish_teller(numlist)
    print("---------------------------")

print("축하합니다. 모든 카드를 맞추셨습니다!")

