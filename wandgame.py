import numpy as np
'''WAND GAME IS BASICALLY JUST TERRORISTS && RIOTERS VS YOU. YOU HAVE A COUPLE MILITARY OPTIONS, WITH NO COSTS (DEFENSE MINISTRY IS LENDING) BUT ALSO 
THEY HAVE DIFFERENT PROBABILITIES OF WORKING. THIS INFORMATION HAS LEAKED TO THE OPPONENT AND THEY WILL KNOW WHAT YOU ARE PICKING AND ALSO
ARE PERFECT LOGICIANS. THE RIOTERS CAN KILL YOUR ARMY OR THE TERRORISTS 70% OF THE TIME, THE TERRORISTS CAN KILL THE RIOTERS/YOUR ARMY 90% OF THE TIME. 
YOU HAVE 3 OPTIONS OF INFANTRY, THE VOLUNTEER FORCES, WHO CAN
KILL 60% OF THE TIME, THE TRAINED FORCES WHO KILL 80% OF THE TIME AND THE ELITE SQUAD WHO KILL 100% OF THE TIME. YOU CAN CHOOSE TO DEPLOY THEM TO EITHER THE RIOTERS
OR THE TERRORISTS AND WITH THE ELEMENT OF SURPRISE, THEY GET TO ATTACK FIRST, BUT YOU CAN ALSO CHOOSE TO NOT ACT. ONCE YOU ARE DONE, THE TERRORISTS WILL AMBUSH 
EITHER YOU OR THE RIOTERS, AND FINALLY THE RIOTERS WILL ATTACK. IF EVERYONE IS ALIVE THOUGH, THE RIOTERS AND TERRORISTS FORM AN ALLIANCE AND OVERTHROW THE
GOVERNMENT. IF THE SITUATION GOES OUT OF CONTROL, THE MILITARY WILL ACT ON ITS OWN AND INCUR MAJOR FINANCIAL LOSS. WHAT ARMY DO YOU PICK?
1. VOLUNTEERS
2. TRAINED
3. ELITE

WHO DO YOU ATTACK?
1. TERRORISTS
2. RIOTERS
3. SIT AROUND

IF VOLUNTEERS && SIT AROUND:
    WIN
ELSE:
    CALCULATE PROBABILITY

'''
import front
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
class terr:
    def __init__(self,prob):
        self.prob = prob
        self.alive = 1
    def target(self,yourprob: float ,riotprob: float,riotalive: int):
        if riotalive:
            if self.prob<yourprob:
                return 4
            else:
                if yourprob>riotprob:
                    return 3
                else:
                    return 2
        else:
            return 3
    def die(self):
        self.alive = 0

class riot:
    def __init__(self,prob):
        self.prob = prob
        self.alive = 1
    def target(self,yourprob: float, terrprob: float,terralive: int):
        if terralive:
            if yourprob<terrprob:
                return 1
            else:
                return 3
        else:
            return 3
    def die(self):
        self.alive = 0
atk = lambda prob : np.random.choice([0,1],p=[1-prob/100,prob/100])
class nullclass:
    def __init__(self):
        self.alive=1
    def die(self):
        pass
class moi:
    def __init__(self,prob):
        self.prob=prob
        self.alive=1
    def die(self):
        self.alive=0
def main(c,a):
    '''c is the choice and a is the attack'''
    mfw = nullclass()
    terrorista = terr(np.random.randint(85,95))
    riota = riot(np.random.randint(65,70))
    d={1:np.random.randint(55,60),2:np.random.randint(75,80),3:100}
    me=moi(d[c])
    d1={1:terrorista,2:riota,3:me,4:mfw}
    i=0
    if c==1 and a==3:
        for i in range(20):
            print()
        print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
                                                        ⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⢀⡴⠋⠀⢀⡤⣖⡫⠭⠭⠭⠭⣍⣑⣒⣒⣒⣻⠭⢝⠲⣄⡀⠀
                                                        ⠀⠀⠀⢀⡾⠁⠠⢖⡽⣪⡑⠬⡭⠭⢙⡄⠀⠀⠀⢐⠒⠒⠒⢤⠀⠀⠹⡄⠀⠀
                                                        ⠀⠀⣠⡞⠁⠀⠀⢈⡜⠁⠁⣠⣭⣄⠐⢈⢦⠀⠀⢠⠒⠈⠉⣩⠉⠲⢄⢷⡀⠀
                                                        ⠀⡴⡻⢛⣩⠥⣄⡙⢆⢀⠄⠛⠿⠋⠀⠅⡼⠁⠲⣇⠁⠀⠺⣿⠗⠀⢄⡧⡹⡆
                                                        ⢸⢱⢀⡏⠀⣰⣄⡉⠀⠉⠒⠛⠓⠚⣚⡉⠀⠀⠀⢯⣐⠠⠴⠤⠄⡒⠛⢸⢰⡇
                                                        ⢸⡄⡈⡇⠉⢻⡀⠙⢳⣦⣄⡉⠉⠁⣏⠤⠦⠄⠀⠀⡽⠇⠄⡀⢀⣿⡄⡊⢲⠇
                                                        ⠀⠻⣌⠒⠀⠈⣿⣶⣬⣧⣀⠉⠙⡷⠶⠤⢤⣄⣘⣛⣁⣠⣤⠖⡏⢻⡇⢠⡏⠀
                                                        ⠀⠀⠘⢧⠀⠀⣿⣿⣿⣿⣿⣿⣶⣧⣤⣀⣸⣇⣀⣸⣀⣀⣼⣤⣿⣾⣷⠘⡇⠀
                                                        ⠀⠀⠀⠘⢧⡀⢸⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀
                                                        ⠀⠀⠀⠀⠈⠻⣆⠹⣌⢻⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀
                                                        ⠀⠀⠀⠀⠀⠀⠈⢳⡈⠻⣀⠀⠈⡟⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡈⠓⢾⣇⡀⠀⢸⡇⠀⢸⠏⠉⡏⢹⣃⣷⠃⢠⠇⠀
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣌⣉⠙⠛⠓⠒⠚⠓⠚⠋⠉⠉⣀⣠⠏⠀⠀
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀

                                              ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗██╗
                                              ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║██║
                                               ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║██║
                                                ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝╚═╝
                                                 ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗██╗
                                                 ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝
============================================================================================================================================================ 
            ''')
        for i in range(5):
            print()
        writeG("You made the wisest choice and won.")
        return 1
    while me.alive:
        [d1[a].die() if atk(d[c]) else 0]
        [[d1[terrorista.target(me.prob,riota.prob,riota.alive)].die() if atk(terrorista.prob) else 0] if terrorista.alive else 0]
        [[d1[riota.target(me.prob,terrorista.prob,terrorista.alive)].die() if atk(riota.prob) else 0] if riota.alive else 0]
        i+=1
        if i==1 and me.alive and terrorista.alive and riota.alive:
            for i in range(20):
                print()
            print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
                                                                ⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠟⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⢷⡄⠈⡓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠂⢹
                                                                ⠈⡷⡄⠈⠲⢤⣈⠻⠉⠛⠉⠉⠁⠒⠖⠉⠉⠉⠒⠶⢦⣤⠴⠒⢉⣡⠴⠀⢀⠏
                                                                ⠀⢸⡿⡂⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⡞⠉⠀⢀⣠⡞⠀
                                                                ⠀⠀⢙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢠⡼⡟⠀⠀
                                                                ⠀⠀⡼⠋⠀⣤⣀⠀⠀⠀⠀⠀⠈⠐⣂⣄⠀⠀⠀⠀⠀⠀⠀⢀⠀⣰⡟⠁⠀⠀
                                                                ⠀⢠⡇⠀⠀⠘⠛⠃⠀⠀⠀⠀⠾⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀
                                                                ⠀⢸⡇⢺⡀⠀⢠⡒⠠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠸⡇⠀⠀⠀
                                                                ⠀⢸⡇⣘⠑⡀⠀⠙⢏⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⣔⣇⠀⠀⠀
                                                                ⠀⢸⡇⡁⠀⢳⣶⣾⣷⣦⣄⣀⡀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀
                                                                ⠀⠸⡇⠁⠀⠀⢏⠉⠀⠀⠙⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠀⠀⠀
                                                                ⠀⠀⠯⣀⣈⣀⣈⣐⣲⣄⣄⣤⣴⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣛⡧⠀⠀⠀
                                             
                                            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗██╗██╗
                                            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝██║██║
                                             ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   ██║██║
                                              ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   ╚═╝╚═╝
                      .                        ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   ██╗██╗
                                               ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝
============================================================================================================================================================
            ''')
            for i in range(5):
                print()
            writeR("You did not make the best choice and unfortunately lost.")
            return 0
        if i==2 and me.alive and (terrorista.alive or riota.alive):
            for i in range(20):
                print()
            print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
                                                                ⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠟⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⢷⡄⠈⡓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠂⢹
                                                                ⠈⡷⡄⠈⠲⢤⣈⠻⠉⠛⠉⠉⠁⠒⠖⠉⠉⠉⠒⠶⢦⣤⠴⠒⢉⣡⠴⠀⢀⠏
                                                                ⠀⢸⡿⡂⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⡞⠉⠀⢀⣠⡞⠀
                                                                ⠀⠀⢙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢠⡼⡟⠀⠀
                                                                ⠀⠀⡼⠋⠀⣤⣀⠀⠀⠀⠀⠀⠈⠐⣂⣄⠀⠀⠀⠀⠀⠀⠀⢀⠀⣰⡟⠁⠀⠀
                                                                ⠀⢠⡇⠀⠀⠘⠛⠃⠀⠀⠀⠀⠾⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀
                                                                ⠀⢸⡇⢺⡀⠀⢠⡒⠠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠸⡇⠀⠀⠀
                                                                ⠀⢸⡇⣘⠑⡀⠀⠙⢏⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⣔⣇⠀⠀⠀
                                                                ⠀⢸⡇⡁⠀⢳⣶⣾⣷⣦⣄⣀⡀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀
                                                                ⠀⠸⡇⠁⠀⠀⢏⠉⠀⠀⠙⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠀⠀⠀
                                                                ⠀⠀⠯⣀⣈⣀⣈⣐⣲⣄⣄⣤⣴⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣛⡧⠀⠀⠀
                                             
                                            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗██╗██╗
                                            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝██║██║
                                             ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   ██║██║
                                              ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   ╚═╝╚═╝
                      .                        ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   ██╗██╗
                                               ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝
============================================================================================================================================================
            ''')
            for i in range(5):
                print()
            writeR("You did not make the best choice and unfortunately lost.")
            return 0
        if me.alive and not (terrorista.alive and riota.alive):
            for i in range(20):
                print()
            print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
                                                        ⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
                                                        ⠀⠀⠀⠀⢀⡴⠋⠀⢀⡤⣖⡫⠭⠭⠭⠭⣍⣑⣒⣒⣒⣻⠭⢝⠲⣄⡀⠀
                                                        ⠀⠀⠀⢀⡾⠁⠠⢖⡽⣪⡑⠬⡭⠭⢙⡄⠀⠀⠀⢐⠒⠒⠒⢤⠀⠀⠹⡄⠀⠀
                                                        ⠀⠀⣠⡞⠁⠀⠀⢈⡜⠁⠁⣠⣭⣄⠐⢈⢦⠀⠀⢠⠒⠈⠉⣩⠉⠲⢄⢷⡀⠀
                                                        ⠀⡴⡻⢛⣩⠥⣄⡙⢆⢀⠄⠛⠿⠋⠀⠅⡼⠁⠲⣇⠁⠀⠺⣿⠗⠀⢄⡧⡹⡆
                                                        ⢸⢱⢀⡏⠀⣰⣄⡉⠀⠉⠒⠛⠓⠚⣚⡉⠀⠀⠀⢯⣐⠠⠴⠤⠄⡒⠛⢸⢰⡇
                                                        ⢸⡄⡈⡇⠉⢻⡀⠙⢳⣦⣄⡉⠉⠁⣏⠤⠦⠄⠀⠀⡽⠇⠄⡀⢀⣿⡄⡊⢲⠇
                                                        ⠀⠻⣌⠒⠀⠈⣿⣶⣬⣧⣀⠉⠙⡷⠶⠤⢤⣄⣘⣛⣁⣠⣤⠖⡏⢻⡇⢠⡏⠀
                                                        ⠀⠀⠘⢧⠀⠀⣿⣿⣿⣿⣿⣿⣶⣧⣤⣀⣸⣇⣀⣸⣀⣀⣼⣤⣿⣾⣷⠘⡇⠀
                                                        ⠀⠀⠀⠘⢧⡀⢸⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀
                                                        ⠀⠀⠀⠀⠈⠻⣆⠹⣌⢻⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀
                                                        ⠀⠀⠀⠀⠀⠀⠈⢳⡈⠻⣀⠀⠈⡟⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡈⠓⢾⣇⡀⠀⢸⡇⠀⢸⠏⠉⡏⢹⣃⣷⠃⢠⠇⠀
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣌⣉⠙⠛⠓⠒⠚⠓⠚⠋⠉⠉⣀⣠⠏⠀⠀
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀

                                              ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗██╗
                                              ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║██║
                                               ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║██║
                                                ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝╚═╝
                                                 ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗██╗
                                                 ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝
============================================================================================================================================================ 
            ''')
            for i in range(5):
                print()
            writeG("You did not make the wisest choice but luckily won.")
            return 1
        if i==2:
            break
    for i in range(20):
        print()
    print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
                                                                ⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠟⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⢷⡄⠈⡓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠂⢹
                                                                ⠈⡷⡄⠈⠲⢤⣈⠻⠉⠛⠉⠉⠁⠒⠖⠉⠉⠉⠒⠶⢦⣤⠴⠒⢉⣡⠴⠀⢀⠏
                                                                ⠀⢸⡿⡂⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⡞⠉⠀⢀⣠⡞⠀
                                                                ⠀⠀⢙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢠⡼⡟⠀⠀
                                                                ⠀⠀⡼⠋⠀⣤⣀⠀⠀⠀⠀⠀⠈⠐⣂⣄⠀⠀⠀⠀⠀⠀⠀⢀⠀⣰⡟⠁⠀⠀
                                                                ⠀⢠⡇⠀⠀⠘⠛⠃⠀⠀⠀⠀⠾⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀
                                                                ⠀⢸⡇⢺⡀⠀⢠⡒⠠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠸⡇⠀⠀⠀
                                                                ⠀⢸⡇⣘⠑⡀⠀⠙⢏⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⣔⣇⠀⠀⠀
                                                                ⠀⢸⡇⡁⠀⢳⣶⣾⣷⣦⣄⣀⡀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀
                                                                ⠀⠸⡇⠁⠀⠀⢏⠉⠀⠀⠙⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠀⠀⠀
                                                                ⠀⠀⠯⣀⣈⣀⣈⣐⣲⣄⣄⣤⣴⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣛⡧⠀⠀⠀
                                             
                                            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗██╗██╗
                                            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝██║██║
                                             ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   ██║██║
                                              ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   ╚═╝╚═╝
                                               ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   ██╗██╗
                                               ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝
============================================================================================================================================================
            ''')
    for i in range(5):
        print()
    writeR("You did not make the best choice and unfortunately lost.")        
    return 0
for i in range(45):
    print()
writeY("WAND GAME IS BASICALLY JUST TERRORISTS & RIOTERS VS YOU. YOU HAVE A COUPLE MILITARY OPTIONS, WITH NO COSTS (DEFENSE MINISTRY IS LENDING) BUT ALSO THEY HAVE DIFFERENT PROBABILITIES OF WORKING. THIS INFORMATION HAS LEAKED TO THE OPPONENT AND THEY WILL KNOW WHAT YOU ARE PICKING AND ALSO ARE PERFECT LOGICIANS. THE RIOTERS CAN KILL YOUR ARMY OR THE TERRORISTS 70% OF THE TIME, THE TERRORISTS CAN KILL THE RIOTERS/YOUR ARMY 90% OF THE TIME. YOU HAVE 3 OPTIONS OF INFANTRY, THE VOLUNTEER FORCES, WHO CAN KILL 60% OF THE TIME, THE TRAINED FORCES WHO KILL 80% OF THE TIME AND THE ELITE SQUAD WHO KILL 100% OF THE TIME. YOU CAN CHOOSE TO DEPLOY THEM TO EITHER THE RIOTERS OR THE TERRORISTS AND WITH THE ELEMENT OF SURPRISE, THEY GET TO ATTACK FIRST, BUT YOU CAN ALSO CHOOSE TO NOT ACT. ONCE YOU ARE DONE, THE TERRORISTS WILL AMBUSH EITHER YOU OR THE RIOTERS, AND FINALLY THE RIOTERS WILL ATTACK. IF EVERYONE IS ALIVE THOUGH, THE RIOTERS AND TERRORISTS FORM AN ALLIANCE AND OVERTHROW THE GOVERNMENT. IF THE SITUATION GOES OUT OF CONTROL, THE MILITARY WILL ACT ON ITS OWN AND INCUR MAJOR FINANCIAL LOSS. ")
time.sleep(4)
for i in range(2):
    print()
print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
''')
for i in range(2):
    print()
print(Fore.YELLOW+Style.BRIGHT+'''
                                                    +-----------------------------------------------------------------+
                                                    |         CHOICE NUMBER         |          ARMY CHOICE            |
                                                    |=================================================================|
                                                    |               1               |          VOLUNTEERS             |
                                                    |-----------------------------------------------------------------|
                                                    |               2               |           TRAINED               |
                                                    |-----------------------------------------------------------------|
                                                    |               3               |            ELITE                |
                                                    +-----------------------------------------------------------------+
''')
for i in range(2):
    print()
print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
''')
for i in range(2):
    print()
writeY("WHAT ARMY DO YOU PICK?")
c=int(input())
for i in range(2):
    print()
print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
''')
for i in range(2):
    print()
print(Fore.YELLOW+Style.BRIGHT+'''
                                                    +-----------------------------------------------------------------+
                                                    |         CHOICE NUMBER         |          ARMY CHOICE            |
                                                    |=================================================================|
                                                    |               1               |           TERRORISTS            |
                                                    |-----------------------------------------------------------------|
                                                    |               2               |             RIOTERS             |
                                                    |-----------------------------------------------------------------|
                                                    |               3               |           SIT SROUND            |
                                                    +-----------------------------------------------------------------+
''')
for i in range(2):
    print()
print(Fore.YELLOW+Style.BRIGHT+'''
============================================================================================================================================================
''')
for i in range(2):
    print()
writeY("WHO DO YOU ATTACK?")
a=int(input())
main(c,a)

    
