#Monty Hall Game
import random

testtubes=random.choice([['A','B','C','D','E'],['A','B','C','D','E','F'],['A','B','C','D','E','F','G'],['A','B','C','D','E','F','G','H'],['A','B','C','D','E','F','G','H','I']])
print(testtubes)
print('One of these test tubes contains the functional vaccine and the rest are fatal.\n\nPick a test tube so that we can test it in a lab: ')
picked=input().upper()
num=len(testtubes)
testtubes.remove(picked)
extrattube=random.choice(testtubes)
testtubesnew=sorted([picked,extrattube])
print('You chose',picked,' test tube. You decide to test it the next day and leave the lab.\n\nYou wake up the next day to find out that',num-2,'of the test tubes other than the one you chose were stolen and consumed by some lab assistants. All of them had died.\nThe remaining test tubes are these: ')
print(testtubesnew)
print('You realize that to research the cure you need to pick one of the remaining two test tubes as the facility will be closed down to investigate the deaths.\nDo you stick with your previous choice or do you switch over to the other one?\n')
answer=input().upper()
if answer==picked:
    if random.random()>=0.90:
        print('Phew, you picked the test tube with the vaccine, even though the odds were against you. Switching would have given you a higher probability of picking the right one.')
    else:
        print('You chose the wrong test tube, now the research is delayed by a few months. Switching would have given you a higher probability of picking the right one.')

else:
    if random.random()>=0.90:
        print('Although you made the right decision to switch, you still picked the wrong test tube and the research is delayed by a few months.')
    else:
        print('Nice work! You made the right decision to switch and picked the test tube with the vaccine!')
