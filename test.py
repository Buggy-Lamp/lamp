import urllib.request, json
from magicblue import MagicBlue
import config
from utils import writeToLog


def talk_to_lamp():
    bulb_mac_address = config.mac
    writeToLog("Connecting to bulb at address {}".format(bulb_mac_address))
    # version is 10 assuming all lamps deployed will be the same
    bulb = MagicBlue(bulb_mac_address, 10)
    try:
        bulb.connect()
    except:
        writeToLog("!!!SEVERE!!!\n something went wrong connecting to lamp \n !!!SEVERE!!!")
    try:
        with urllib.request.urlopen(config.url) as url:
            data = json.loads(url.read().decode())
            color = data['color']

        if color == "red":
            print("setting lamp to --RED--")
            writeToLog("setting lamp to --RED--")
            bulb.set_color([255, 0, 0])
        elif color == "green":
            bulb.set_color([0, 255, 0])
            print("setting lamp to --GREEN--")
            writeToLog("setting lamp to --GREEN--")
        elif color == "orange":
            bulb.set_color([255, 165, 0])
            print("setting lamp to --ORANGE--")
            writeToLog("setting lamp to --ORANGE--")
        else:
            bulb.set_color([0, 0, 255])
            print("INVALID color setting lamp to --BLUE--")
            writeToLog("INVALID color setting lamp to --BLUE--")
    except:
        print("couldn't get data from API setting lamp to --BLUE--")
        writeToLog("couldn't get data from API setting lamp to --BLUE--")
        bulb.set_color([0, 0, 255])
