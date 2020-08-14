import config
from setup import InitialFunction
import os


def Run():
    firstTime()


def firstTime():
    if os.path.isfile("~/config.txt"):
        reset = input("It seems like you already set everything up do you wanna do it again?")
        if validate(reset):
            reset_config()
        else:
            exit()
    else:
        start_setup()


def start_setup():
    print("""               _               __  __ _____     _____ ______ _______ _    _ _____  
                      | |        /\   |  \/  |  __ \   / ____|  ____|__   __| |  | |  __ \ 
                      | |       /  \  | \  / | |__) | | (___ | |__     | |  | |  | | |__) |
                      | |      / /\ \ | |\/| |  ___/   \___ \|  __|    | |  | |  | |  ___/ 
                      | |____ / ____ \| |  | | |       ____) | |____   | |  | |__| | |     
                      |______/_/    \_\_|  |_|_|      |_____/|______|  |_|   \____/|_| \n""")
    ask_setup_url()



def reset_config():
    file = open("config.txt","w")
    file.close()
    print("Config file emptied.")

    start_setup()


def validate(userInput):
    if userInput == "Y" or userInput == "y":
        return True
    elif userInput == "N" or userInput == "n":
        return False
    else:
        print("Please select either Y or N")


def ask_setup_url():
    s = input("please input setup Url \n")
    print(f"is this the correct URL? \n {s}")
    url_ans = input("Y/N \n")
    if validate(url_ans):
        config.setupUrl = s
        ask_log_path()
    else:
        ask_setup_url()


def ask_log_path():
    print("where would you like to save your logs please provide the full path")
    print("Example : /home/pi/Desktop")
    s = input()
    s.replace("\\","/")
    print(f"is this the correct Path? \n {s}")
    path_ans = input("Y/N \n")
    if os.path.exists(s) and "\\" not in s:
        if validate(path_ans):
            config.logFile = s + "/LampLogs.txt"
            print(config.logFile)
            InitialFunction()
        else:
            ask_log_path()
    else:
        print("This path doesn't exist try again \n")
        ask_log_path()


Run()
