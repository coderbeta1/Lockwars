import getpass
import pandas as pd
import numpy as np

def login_check(username_inp,password_inp,method):
        user_logs=pd.read_csv("user_logs.csv")
        if username_inp in list(user_logs['USERNAME']):
            if method==2:
                print("Username Already Exists. Please Retry")
                welcome_screen()
            pos=list(user_logs['USERNAME']).index(username_inp)
            if user_logs.iloc[pos]['PASSWORD']!=password_inp:
                print("Incorrect Username or Password. Please Retry")
                welcome_screen()
            else:
                return
        else:
            if method==2:
                return
            print("Unknown Username. Please Retry")
            welcome_screen()
def welcome_screen():
    print('''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                LOGIN/SIGNUP
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                               +---------------------------------------------------------------------+
                                               |           *1.LOGIN                                                  |
                                               |           *2.SIGNUP                                                 |
                                               |           *3.EXIT                                                   |                                        |
                                               +---------------------------------------------------------------------+

                 ''')
    log_sign=int(input("What do you wish to do: "))
    if log_sign==1:
        login()
    elif log_sign==2:
        signup()
    elif log_sign==3:
        exit()

def login():
    print('''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                Please Enter Your Username and Password
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                 ''')
    username_inp=input('''USERNAME: ''')
    password_inp=getpass.getpass(prompt='''PASSWORD:  ''')
    login_check(username_inp,password_inp,1)

def signup():
    username_inp=input('''USERNAME: ''')
    password_inp=getpass.getpass(prompt='''PASSWORD:  ''')
    login_check(username_inp,password_inp,2)
    f = open("user_logs.csv", "a")
    f.write("\n"+str(np.random.randint(100000000))+","+username_inp+","+password_inp)
    f.close()
    #user_logs.to_csv("user_logs.csv")
    welcome_screen()
