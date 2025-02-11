# Here we fetch initial setup data from an endpoint
# To make the pi connect to the lamp and know where to get status info from
# Think of mac address --> fetch url --> potential lamp id
# Info about cron job python management
# This will also create a cron job upon succession to automatize the retrieval
# https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231#:~:text=Writing%20Your%20First%20Cron%20Job&text=Create%20a%20file%20called%20scheduleCron,into%20the%20scheduleCron.py%20program.&text=Using%20the%20CronTab%20module%2C%20let's%20access%20the%20system%20crontab%20.&text=The%20above%20command%20creates%20an,system%20crontab%20of%20the%20user.

import json
import sys
import time
import urllib.request
from crontab import CronTab
import config
from utils import writeToLog
from lamp_controller import talk_to_lamp


def create_cron_job():
    try:
        my_cron = CronTab(user="pi")
        job = my_cron.new(command="sudo python3 ~/Desktop/lamp/cronjob.py")
        job.minute.every(1)
        my_cron.write()
        print("cron job created")
    except:
        writeToLog("!!!SEVERE!!!\n something went wrong creating the cron job \n !!!SEVERE!!!\n")
        print("failed to create cronjob")


def InitialFunction():
    try:
        f = open("config.txt", "r")
        info = f.readlines()
        config.url = info[0].strip("\n")
        config.mac = info[1].strip("\n")
        config.logFile = info[2].strip("\n")
        f.close()

        print("Config found using previous data" + "\n")
        print(f"lamp mac address : {config.mac}----- URL : {config.url}\n")

        writeToLog("Config found using previous data" + "\n")
        writeToLog(f"lamp mac address : {config.mac}----- URL : {config.url}\n")
        talk_to_lamp()

    except FileNotFoundError:
        print("Starting up attempting to connect to server \n")
        writeToLog("Starting up attempting to connect to server \n")
        try:
            with urllib.request.urlopen(config.setupUrl) as url:

                data = json.loads(url.read().decode())
                config.url = data["url"]
                config.mac = data["mac"]

                print("Retrieved data from server \n")
                print(f"lamp mac address : {config.mac} ----- URL : {config.url} \n")
                writeToLog("Retrieved data from server \n")
                writeToLog(f"lamp mac address : {config.mac} ----- URL : {config.url} \n")

                print("saving to config")
                f = open("config.txt", "a+")
                f.write(config.url + "\n")
                f.write(config.mac + "\n")
                f.write(config.logFile + "\n")
                f.close()

                # we did it boys now lets create a cron job
                print("create cronjob")
                create_cron_job()
                talk_to_lamp()

        except Exception:
            print("Something went wrong getting the data please validate your settings. attempting "
                  "to do it again! in 60 seconds \n")
            writeToLog("Something went wrong getting the data please validate your settings. attempting "
                       "to do it again! \n")
            writeToLog("error type was " + str(sys.exc_info()[0]) + "\n")
            print(f"_________________\n Developer info\n {sys.exc_info()}")
            time.sleep(60)
            InitialFunction()
