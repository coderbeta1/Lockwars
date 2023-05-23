def testing_kit():
    import random
    from tabulate import tabulate
    advantages_val={"Quick results:\nProvides results within 15 minutes.":0.81,"Cost-effective:\nAffordable compared to other testing methods.":0.82,"Easy to use:\nSimple and straightforward testing procedure.":0.83,"High accuracy:\nConsidered the gold standard for virus detection.":0.89,"Increased sensitivity:\nCan detect the virus even at low levels.":0.90,"Long detection window:\nCan identify the virus in the early stages of infection.":0.91,"Portable:\nCan be used in various settings, including remote areas.":0.97,"Easy to interpret:\nResults can be visually assessed without complex equipment.":0.98,"Longer shelf life:\nQuality of test kit remains same for longer duration of time":0.99}
    advantages=list(advantages_val.keys())
    advantages_shuffled = random.sample(advantages, 9)
    sick_population= random.uniform(0.001, 0.01)
    ran_vals=[]
    for i in range(0,3):
        unit=[0,0]
        unit[0]=random.uniform(0,00.05)
        unit[1]=random.uniform(0.00,0.01)
        ran_vals.append(unit)
    false_negative=[]
    for dataset in ran_vals:
        false_neg=(dataset[0]*sick_population)/((dataset[0]*sick_population)+((1-dataset[1])*(1-sick_population)))
        false_negative.append(false_neg)
    rela={}
    for i in range(0,3):
        rela[false_negative[i]]=ran_vals[i]    
    kit_multiplier=[]
    for j in range(0,3):
        adv_sum=sum(advantages_val[advantages_shuffled[(j)*3+i]] for i in range(0,3))
        kit_multiplier.append(adv_sum)
    score={}
    kit_multiplier_sorted=sorted(kit_multiplier)
    false_negative_sorted=sorted(false_negative,reverse=True)
    for i in range(0,3):
        score[kit_multiplier_sorted[i]]=false_negative_sorted[i]
    test_type_data=[["1","Test Kit A","1)"+advantages_shuffled[0]+"\n"+"2)"+advantages_shuffled[1]+"\n"+"3)"+advantages_shuffled[2],rela[score[kit_multiplier[0]]][0],rela[score[kit_multiplier[0]]][1]],["2","Test Kit B","1)"+advantages_shuffled[3]+"\n"+"2)"+advantages_shuffled[4]+"\n"+"3)"+advantages_shuffled[5],rela[score[kit_multiplier[1]]][0],rela[score[kit_multiplier[1]]][1]],["3","Test Kit C","1)"+advantages_shuffled[6]+"\n"+"2)"+advantages_shuffled[7]+"\n"+"3)"+advantages_shuffled[8],rela[score[kit_multiplier[2]]][0],rela[score[kit_multiplier[2]]][1]]]
    headers_kit=["Test Type No.","Test Name","Advantages","Probability of negative\ntest given person has disease","Probability of positive test\ngiven person does not have the disease"]
    kit_table = tabulate(test_type_data, headers_kit, tablefmt="grid")
    print(kit_table)
    kit_type_choice=int(input("Enter Test Type No. of choice such that the kit is the most optimal:"))
    if kit_multiplier[kit_type_choice-1]==kit_multiplier_sorted[2]:
        print("You chose the best and most optimal answer.")
    elif kit_multiplier[kit_type_choice-1]==kit_multiplier_sorted[1]:
        print("You chose the second most optimal answer.")
    elif kit_multiplier[kit_type_choice-1]==kit_multiplier_sorted[0]:
        print("You chose the least optimal answer.")
    
testing_kit()
