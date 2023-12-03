def finish_teller(input_list):
    input_list=[i for j in input_list for i in j]
    while (" " in input_list):
        input_list.remove(" ")
    print(input_list)
    return len(input_list)==len(set(input_list))

list2=[[" "," "],[" "," "]]
print(finish_teller(list2))