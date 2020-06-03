from datetime import datetime

import config


def getDate():
    now = datetime.now()
    return "[" + now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] + "]"


def writeToLog(message):
    f = open(config.logFile, "a+")
    f.write(getDate() + " " + message)
    f.close()
