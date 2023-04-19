from LeechClass import LeechBot
from CommandClass import basicCommands, leechCommands
import keyboard
import time

leechBot = LeechBot("WF Alt 2",567,0)

if __name__ == '__main__':
    while keyboard.is_pressed("shift+q") != True:
        try:
            problemList = []
            if leechBot.findParentWindow() == False:
                leechBot.openWorldFlipper()
            leechCommands(leechBot)
            basicCommands(leechBot)
        except Exception as e:
            print(e)
            if leechBot.findParentWindow() == False:
                    leechBot.openWorldFlipper()