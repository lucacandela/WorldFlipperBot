from HostClass import HostBot
from CommandClass import basicCommands, hostCommands
import keyboard
import time

hostBot = HostBot("WF Alt 1",567,0)

if __name__ == '__main__':
    while keyboard.is_pressed("shift+q") != True:
        try:
            problemList = []
            if hostBot.findParentWindow() == False:
                hostBot.openWorldFlipper()
            hostCommands(hostBot)
            basicCommands(hostBot)
        except Exception as e:
            print(e)
            if hostBot.findParentWindow() == False:
                    hostBot.openWorldFlipper()