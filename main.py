import time
import login

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

def command_input():
        print('''
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
        print("NOTE: The game will run in the background. React Fast...\n")
        command_input=int(input("What do you wish to do: "))
        if command_input==1:
            mapper()
        elif command_input==2:
            status()
        elif command_input==3:
            eco()
        elif command_input==4:
            resource_tab()
        elif command_input==5:
            mobility()
        elif command_input==6:
            save()
        elif command_input==7:
            exit()

def main():
    login.welcome_screen()
    command_input()

main()
