'''
Minigame affecting vaxx efficiency. Runs when vaxx progress finishes
n no. of variants, min no. of ppl to take so that p(2 w same)>=50%
'''

import random as rn,math
state={}
def bday(n,x):
    return 1-math.factorial(n)/(math.factorial(n-x)*n**x)
def findanswer(n):
    for x in range(10,n):
        if bday(n,x)>=0.9 and bday(n,x-1)<0.9:
            return x
def event(state):
    n=rn.randint(20, 40)
    print(f'There are {n} new variants in town. In order to get a better look at them you decide to conduct a study taking a few random\
 travellers from the airport. But people are busy and hence you must try to take as less people as possible. What is the minimum\
 number of people you should take so the chance that at least two of the participants have the same variant is at greater than 90%') #make 'n' stand out
    x=int(input())       #take input as x
    if bday(n,x)>=0.9 and bday(n,x-1)<0.9:
        print('Good Work! Thanks to your help the researchers were able to improve the vaccine')
        state['vaxxeff']=int(rn.randint(85, 95)/100)
    else:
        ans=findanswer(n)
        print(f"Nice Try! The optimal number of people is {ans}. You can find the answer by finding the probability that no two people\
 have the same variant and subtracting it from the total probability")
        state['vaxxeff']=int(rn.randint(70, 85)/100)
    return state
event(state)        #remove when integraing