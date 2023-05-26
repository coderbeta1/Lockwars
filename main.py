import front
import time
import login
import sys
import colorama
from PIL import Image
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def loop(queue):
     state=queue.get()
     p=input()
     i=input()
     if p==4:
          state[i]['eco'] = input()
     queue.put(state)

def mapper():
    return

def status():
    return

def eco():
    return

def resource_tab():
    return

def mobility():
    return

def save():
    return

def write(write):
    for i in write:
        print(Fore.YELLOW+i,end="")
        sys.stdout.flush()
        time.sleep(.02)
    print()

def story():
    for i in range(45):
        print()
    write('''
    In "BioArmory – Survive the Epidemic", the world is in the grip of a deadly and rapidly spreading epidemic. As a brilliant scientist and renowned epidemiologist,
    you have been tasked with leading the global effort to find a cure and save humanity from the brink of disaster.Your journey begins as you discover a new strain
    of virus, which reports a rising number of infections and increasing mortality rates. The world is in a state of panic, and public distrust is growing as
    misinformation spreads like wildfire.Your mission is to obtain a complete cure for the virus, collaborating with local health agencies, governments, and research
    institutions to gather vital data and resources. Along the way, you must manage limited healthcare capacities, navigate economic challenges, and address public
    distrust.

    Can you analyse the complex web of factors, maintain global stability, and ultimately find the cure to save humanity? The clock is ticking, and the world is
    looking to you for leadership ??
''')
    time.sleep(5)

def command_input(queue):
        for i in range(40):
            print()
        print(Fore.YELLOW+'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                Please select a command from Below
------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                               +---------------------------------------------------------------------+
                                               |           *1.Current Map                                            |
                                               |           *2.Current Status                                         |
                                               |           *3.Economic Details                                       |
                                               |           *4.Resource Allocation                                    |
                                               |           *5.Mobility                                               |
                                               |           *6.Save Current Progress                                  |
                                               |           *7.Close Programme                                        |
                                               +---------------------------------------------------------------------+

                     ''')
        print(Fore.YELLOW+'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                    NOTE: Game will run in the background. React Fast...
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        ''')

        for i in range(7):
            print()
        command_input=int(input("What do you wish to do: "))
        if command_input==1:
            img=Image.open('breh.jpeg')
            img.show()
        elif command_input==2:
            print("ECO: "state['eco'],"INFECTED: ",state['totinfect'],"DEAD: "state['totdead'])
        elif command_input==3:
            state=queue
        elif command_input==4:
            state=queue.get()
        elif command_input==5:
            state=queue.get()
        elif command_input==6:
            state=queue.get()
        elif command_input==7:
            front.thank_you()
            exit()
        return state
def main(queue):
    front.introduction()
    login.welcome_screen()
    story()
    queue.put(1)
    while True:
        state=queue.get()
        state=command_input(state)
        queue.put(state)

main()
