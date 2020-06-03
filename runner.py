import config
from setup import InitialFunction
from os import path


def Run():
    print("""               _               __  __ _____     _____ ______ _______ _    _ _____  
              | |        /\   |  \/  |  __ \   / ____|  ____|__   __| |  | |  __ \ 
              | |       /  \  | \  / | |__) | | (___ | |__     | |  | |  | | |__) |
              | |      / /\ \ | |\/| |  ___/   \___ \|  __|    | |  | |  | |  ___/ 
              | |____ / ____ \| |  | | |       ____) | |____   | |  | |__| | |     
              |______/_/    \_\_|  |_|_|      |_____/|______|  |_|   \____/|_| \n""")
    print("Please note you can only fully run this setup once. \nIf you make any mistake and notice too late please "
          "terminate the process")
    print("If however you do fully run through the setup and only notice your mistake afterwards \nplease delete the "
          "config.txt file that should be located under the default users home folder by default : /home/pi/Downloads \n")
    ask_setup_url()


def validate(userInput):
    if userInput == "Y" or userInput == "y":
        return True
    elif userInput == "N" or userInput == "n":
        return False
    else:
        print("Please select either Y or N")


def ask_setup_url():
    s = input("please input setup Url \n")
    print("is this the correct URL? \n" + s)
    url_ans = input("Y/N \n")
    if validate(url_ans):
        config.setupUrl = s
        ask_log_path()
    else:
        ask_setup_url()


def ask_log_path():
    print("where would you like to save your logs please provide the full path")
    print("do NOT add any / or \\ to the end and DONT specify a file name just the location")
    print("path with forwards slashes \"/\" not \"\\\"")
    print("Example : /home/pi/Desktop")
    s = input()
    print("is this the correct Path? \n" + s)
    path_ans = input("Y/N \n")
    if path.exists(s) and "\\" not in s:
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
