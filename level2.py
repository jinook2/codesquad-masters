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

def result():
    print("게임 종료! {}:{}점, {}:{}점".format(player1,player_score[0],player2,player_score[1]))
    if (player_score[0]==player_score[1]):
        print("무승부!")
    elif(player_score[0]>player_score[1]):
        print("{}승리".format(players[0]))
    elif(player_score[0]<player_score[1]):
        print("{}승리".format(players[1]))

player1=input("1P의 이름을 입력하세요")
player2=input("2P의 이름을 입력하세요")
players=[player1,player2]

notarranged_numlist=num_gen()
numlist=num_arrange(notarranged_numlist)
doublelist_displayer(numlist)
player_list=[["x"]*6,["x"]*6,["x"]*6]

player_index=0
player_score=[0,0]

i=0
combo=0
while (finish_teller(numlist) !=True):
    i=i+1
    displayed_list=copy.deepcopy(player_list)
    doublelist_displayer(displayed_list)
    print()
    player=players[player_index]
    print("{} 차례, combo:{}, score:{}".format(player,combo,player_score[player_index]))
    print("<시도 {}, 남은 카드: {}> 좌표를 두 번 입력하세요".format(i,x_counter(player_list)))
    input1=input("입력 1? ").strip("()").split(",")
    input1=[int(input1[0])-1,int(input1[1])-1]
    input2=input("입력 2? ").strip("()").split(",")
    input2=[int(input2[0])-1,int(input2[1])-1]
    if input1==input2:
        raise Exception("서로 다른 카드를 뽑으십시오")
    if numlist[input1[0]][input1[1]]==" " or numlist[input2[0]][input2[1]]==" ":
        raise Exception("존재하지 않는 카드입니다")

    displayed_list[input1[0]][input1[1]]=numlist[input1[0]][input1[1]]
    displayed_list[input2[0]][input2[1]]=numlist[input2[0]][input2[1]]
    doublelist_displayer(displayed_list)

    if (numlist[input1[0]][input1[1]]==numlist[input2[0]][input2[1]]):
        player_list[input1[0]][input1[1]]=" "
        player_list[input2[0]][input2[1]]=" "
        numlist[input1[0]][input1[1]]=" "
        numlist[input2[0]][input2[1]]=" "        
        print("정답!")
        combo+=1
        player_score[player_index]+=10*(2**(combo-1))
    else:
        player_index=(player_index+1)%2
        combo=0
        print("땡")
    finish_teller(numlist)
    print("---------------------------")

result()

# 8 5 1 7 4 7 
# 5 7 3 6 3 4 
# 5 4 8 3 6 2 