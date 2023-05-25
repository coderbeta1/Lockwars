import front as f
import math
import random
import time
import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)
f.event_start()
for i in range(30):
    print()
print(Fore.RED+Style.BRIGHT+'''
    ============================================================================================================================================================

                                                                            
                                                                                                             
                                                                ░░░░▒░░░░░░░░░░░░▒▓▒░░░░░▒▒▓▓▓▓▓▓░░░░░░░░▒░░░
                                                                ░░▓██▓▒░░░░░░░░░░░▓█▓░░▒▓▓▓▓▓▓▓▓▒░░░░░░▒███▒░
                                                                ░██████▓▒░░░░░░░░░░▒█▓▓▓▓▓▓▓▓▓▓▒░░░░░▒██████▓
                                                                ░░▒██████▓▒░░░░░░░░░▒█▓▓▓▓▓▓▓▒▒░░░░▒██████▓░░
                                                                ░░░░▒██████▓▒░░░░░░░░▓█▓▒▒▒▒░░░░░▒██████▓░░░░
                                                                ░░░░░░▒████████▓▓▓▓▓▒▒█▒░▒▓▓▓▓████████▓░░░░░░
                                                                ░░░░░░▒▓█████████▓▓▓▓▓█▓▓▓▓▓██████████▓▒░░░░░
                                                                ░░░░▒▓▓▓▓▓█████████▓▓▓▓▓▓▓██████████▓▓▓▓▓░░░░
                                                                ░░░▒▓▓▓▓▓▓▓▓█████████▓▓▓██████████▓▓▓▓▓▓▓▓░░░
                                                                ░░░▓▓▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▓▓░░
                                                                ░░▒▓▓▓▓▓▓▓▓▓▓▓▓███████████████▓▓▓▓▓▓▓▓▓▓▓▓▓░░
                                                                ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
                                                                ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
                                                                ░░▒▓▓▓▓▓▓▓▓▓▓▓█████████████████▓▓▓▓▓▓▓▓▓▓▓▓░░
                                                                ░░░▓▓▓▓▓▓▓▓▓██████████▓▓█████████▓▓▓▓▓▓▓▓▓▒░░
                                                                ░░░▒▓▓▓▓▓▓██████████▓▓▓▓▓▓█████████▓▓▓▓▓▓▓░░░
                                                                ░░░░▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓█████████▓▓▓▓░░░░
                                                                ░░░░░▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████▓▒░░░░
                                                                ░░░░░▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▒░░░░
                                                                ░░░▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▒░░
                                                                ░▓██████▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓██████▒
                                                                ░▒████▓░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░▒▓███▓▒

                                                                                            

                                    ███████╗ ██████╗  ██████╗ ██████╗     ███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗ █████╗  ██████╗ ███████╗
                                    ██╔════╝██╔═══██╗██╔═══██╗██╔══██╗    ██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝
                                    █████╗  ██║   ██║██║   ██║██║  ██║    ███████╗███████║██║   ██║██████╔╝   ██║   ███████║██║  ███╗█████╗  
                                    ██╔══╝  ██║   ██║██║   ██║██║  ██║    ╚════██║██╔══██║██║   ██║██╔══██╗   ██║   ██╔══██║██║   ██║██╔══╝  
                                    ██║     ╚██████╔╝╚██████╔╝██████╔╝    ███████║██║  ██║╚██████╔╝██║  ██║   ██║   ██║  ██║╚██████╔╝███████╗
                                    ╚═╝      ╚═════╝  ╚═════╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                                                                                      

    ============================================================================================================================================================
                                                                                           ''')
time.sleep(3)
for i in range(50):
    print()
def food_shortage():
    time.sleep(1)
    x=random.randint(27,34)
    print(Fore.YELLOW+Style.BRIGHT+'''
    +----------------------------------------------------------------------------------------------------------------------------------------------------------+
    ''')
    f.write("Due to the pandemic, most of the people in the slum areas lost their jobs, so the government sends food rations every 30 days. You have enough food rations left for "+str(x)+" days. The central government advices that if probability of food reaching is greater than 60%,then it would be advisable to not trouble the government.")
    print()
    print()
    time.sleep(1)
    mean=30
    # choices=[1,0]
    # weights=[cumulative_poisson_probability(mean, x),1-cumulative_poisson_probability(mean, x)]
    # food_arrival=random.choices(choices,weights=weights, k=1)[0]
    print(Fore.GREEN+Style.BRIGHT+'''
                                                                +---------------------------------+
                                                                | Choice number  |     choice     |
                                                                |=================================|
                                                                |       1        | Re-ration now  |
                                                                |================|================|
                                                                |       2        |   Let it be    |
                                                                +---------------------------------+
    ''')
    print('\n\n')
    time.sleep(0.3)
    action=int(input("Enter choice number:"))
    time.sleep(0.5)
    if (cumulative_poisson_probability(mean, x)<=0.6) and (action==1):
        chan=random.random()
        if chan<=0.85:
            print(Fore.GREEN+Style.BRIGHT+'''You made the correct choice to re-ration the food and luckily the food arrived on time.''')
        else:
            print(Fore.GREEN+Style.BRIGHT+'''You made the correct choice to re-ration the food'''+Fore.RED+Style.BRIGHT+''' but unluckily the food did not arrive on time and a lot of people dies of hunger.''')
    elif (cumulative_poisson_probability(mean, x)<=0.6) and (action==2):
        print(Fore.RED+Style.BRIGHT+'''You made the incorrect choice. Unluckily the food did not arrive on time and a lot of people died of hunger.''')
    elif (cumulative_poisson_probability(mean, x)>0.6) and (action==1):
        chan=random.random()
        if chan<=0.85:
            print(Fore.RED+Style.BRIGHT+'''You made the incorrect choice as the food would have arrived on time anyways but you had to pay a lot of extra money to get it delivered early.''')
        else:
            print(Fore.RED+Style.BRIGHT+'''You made the incorrect choice as there was enough food to last for '''+x+''' days.'''+Fore.GREEN+Style.BRIGHT+''' But fortunately food did not arrive early so you werent made to pay a lot of extra money.''')
    elif (cumulative_poisson_probability(mean, x)>0.6) and (action==2):
        chan=random.random()
        if chan<=0.85:
            print(Fore.GREEN+Style.BRIGHT+'''You made the correct choice and luckily the next batch food arrived on time.''')
        else:
            print(Fore.GREEN+Style.BRIGHT+'''You made the correct choice'''+Fore.RED+Style.BRIGHT+''' but unluckily the food did not arrive on time due to which many people died of hunger.''')
def poisson_probability(mean, x):
    return (math.exp(-mean) * mean ** x) / math.factorial(x)    
def cumulative_poisson_probability(mean, x):
    cumulative_probability = 0
    for i in range(x + 1):
        cumulative_probability += poisson_probability(mean, i)
    return cumulative_probability
food_shortage()
print(Fore.YELLOW+Style.BRIGHT+'''
    +----------------------------------------------------------------------------------------------------------------------------------------------------------+
\n\n''')
