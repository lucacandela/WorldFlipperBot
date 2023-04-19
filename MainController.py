from LeechClass import LeechBot
from CommandClass import basicCommands, leechCommands
import keyboard
import time

mainBot = LeechBot("WF Main",567,0)

if __name__ == '__main__':
    while keyboard.is_pressed("shift+q") != True:
        try:
            
            if mainBot.findParentWindow() == False:
                mainBot.openWorldFlipper()
            leechCommands(mainBot)
            basicCommands(mainBot)
        except Exception as e:
            print(e)
            if mainBot.findParentWindow() == False:
                    mainBot.openWorldFlipper()