import matplotlib.pyplot as plt
import time
import sys
import numpy as np

def write(write):
    for i in write:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.02)
    print()

reference={0:"education_prompt.txt",1:"healthcare_prompt.txt",2:"housing_prompt.txt",3:"industry_prompt.txt",4:"research_prompt.txt",5:"shopping_prompt.txt",6:"amusement_prompt.txt",7:"coatjobs_prompt.txt",8:"farming_prompt.txt",9:"government_prompt.txt",10:"sports_prompt.txt",11:"tourism_prompt.txt"}
score=0

def prompt(num,score=0):
    prompting=open(reference[num], "r").readlines()[np.random.randint(0,high=len(open(reference[num], "r").readlines()))][:-1]
    if prompting[0]=="0":
        score+=int(prompting[1])
    else:
        score-=int(prompting[1])
    return prompting[2:],score

s=0
#THRESHOLD=11
for i in range(10):
    prom,s=prompt(0,s)
    print(prom,s)
