#The next sports major championship is pending approval, For approval you need to test the players. before the even you 
#decide to to do a controlled study. You know that x percent of people have the virus on average. For proper study you need to have atleast certain number
#of infected along with some uninfected people for the test to pass. You need to decide a suitable sample size. Remember: Each person will cost u something.
import front
from numpy import random
import time
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def writeY(write):
    for i in write:
        print(Fore.YELLOW+i,end="")
        sys.stdout.flush()
        time.sleep(.02)
    print()
def writeR(write):
    for i in write:
        print(Fore.RED+i,end="")
        sys.stdout.flush()
        time.sleep(.02)
    print()
def writeG(write):
    for i in write:
        print(Fore.GREEN+i,end="")
        sys.stdout.flush()
        time.sleep(.02)
    print()
front.event_start()
def controlled_test(costofeach : int, average_infected  : float, threshold : float, budget : int):#costofeach = cost of each person, threshold = the percentage of uninfected thats required at the very least
    #average_infected = probability that the person is infected, on average
    for i in range(10):
        print()
    print(Fore.YELLOW+Style.BRIGHT+f'''
============================================================================================================================================================
                                        
                                        +-------------------------------------------------------------------------------+
                                        |                                                                               |
                                        | Cost to hire each person required for the survey :                         {costofeach} |
                                        |                                                                               |
                                        | Minimum number of uninfected persons required                                 |
                                        | to pass the test                                 :                          {threshold} |
                                        |                                                                               |
                                        | The probability that a person is infected is     :                        {average_infected} |
                                        |                                                                               |
                                        | Your current budget is                           :                        {budget} |
                                        |                                                                               |
                                        +-------------------------------------------------------------------------------+

============================================================================================================================================================
                                                          ''')
    for i in range(10):
        print()
    # print(f"The cost of each person will be {costofeach}. \nThe minimum uninfected persons to pass is {threshold}")
    # print(f"The probability that a person is infected is {average_infected}")
    # print(f"Your current budget is {budget}")
    writeY("What sample size would you like to use? The bigger the sample size, the higher the cost.(put an integer) : ")
    sample_size = int(input())
    run_count = 0
    while True:
        for i in range(2):
            print()
        print(Fore.YELLOW+Style.BRIGHT+'''
------------------------------------------------------------------------------------------------------------------------------------------------------------
''')
        for i in range(2):
            print()
        print()
        run_count += 1
        samples = random.choice([1,0], sample_size, p = [1-average_infected, average_infected])
        cost = costofeach * sample_size
        writeY(f"TEST NUMBER {run_count}")
        writeY(f"The test cost {cost}")
        budget -= cost
        writeY(f"The current remaining budget is {budget}")
        if budget < 0:
            writeR("You went over the budget and can no longer perform tests!")
            for i in range(2):
                print()
            print('''
------------------------------------------------------------------------------------------------------------------------------------------------------------
            ''')
            break;
        else:
            if sum(samples) >= threshold :

                writeG(f"The test has successfully passed as there were {sum(samples)} Uninfected from the sample group.")
                while True:
                    x = input("Would you like to redo the test? You have to get the optimal balance between cost and sample size.(Y/N) : ")
                    x = x.lower()
                    if x == "n" or x == "y":
                        break
                    else:
                        writeY("invalid input")
                if x == "n":
                    writeY("Okay you have chosen to halt testing...")
                    for i in range(2):
                        print()
                    print('''
------------------------------------------------------------------------------------------------------------------------------------------------------------
                    ''')
                    break
                
            else:
                writeR(f"The test did not pass as there were {sum(samples)} Uninfected which is under the threshold of {threshold}")
                while True:
                    x = input("Would you like to redo the test? Note that this will cost you more.(Y/N) : ")
                    x = x.lower()
                    if x == "n" or x == "y":
                        break
                    else:
                        writeY("invalid input")
                if x == "n":
                    writeY("Okay you have chosen to halt testing...")
                    for i in range(2):
                        print()
                    print('''
-----------------------------------------------------------------------------------------------------------------------------------------------------------
                    ''')
                    break
                writeY("redoing the test...")
                writeY("...")
        writeY("|-------------------|")
    return
    time.sleep(3)
controlled_test(10,0.2,6,800)




    

    
    
