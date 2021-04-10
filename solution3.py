def list_div(x,y,a,b):
    first_exp = tuple({x+(1/y)})
    for element in first_exp:
        first_exp_ans = element ** a

    second_exp = tuple({x-(1/y)})
    for element in second_exp:
        second_exp_ans = element ** b

    first_list = [first_exp_ans * second_exp_ans]

    third_exp = tuple({y+(1/x)})
    for element in third_exp:
        third_exp_ans = element ** a

    fourth_exp = tuple({y-(1/x)})
    for element in fourth_exp:
        fourth_exp_ans = element ** b

    second_list = [third_exp_ans * fourth_exp_ans]

    #to divide first list and second list

    final_result = [i/j for i,j in zip(first_list,second_list) ]

    #to return reult
    for x in final_result:
        return x





print(list_div(10,20,3,4))


