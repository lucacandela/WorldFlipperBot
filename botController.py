from LeechClass import LeechBot
from HostClass import HostBot
import concurrent.futures
import multiprocessing
import keyboard
import time

#WF Alt 2 & WF Main calculations were made with a window starting at 567,0
#WF Alt 1 was made with a window starting at 


hostBot = HostBot("WF Alt 1",567,0)
leechBot = LeechBot("WF Alt 2",567,0)
mainBot = LeechBot("WF Main",567,0)

leechList = []
botList = []
leechList.append(leechBot)
leechList.append(mainBot)

botList.append(leechBot)
botList.append(mainBot)
botList.append(hostBot)

def basicCommands(bot):
    bot.findParentWindow()
    bot.tapToStart()
    bot.tapBossFight()
    #bot.tapEventButton("eventbutton1") #uncomment if there's an event going on
    bot.tapDialogueOk1Error()
    bot.tapDialogueOk2Error()
    bot.tapDialogueAbortError()
    bot.tapBlueStacksCloseButton()
    bot.tapDialogueYes()
    bot.tapWorldFlipperIcon()

def hostCommands(bot):
    bot.tapBossButton("orochi")
    bot.tapCoop()
    bot.tapRecruit1()
    bot.tapRecruit2()
    bot.tapStart(leechBot) #pass in the leechBot because it looks at its name
    bot.exitMatch(0.0)

def leechCommands(bot):
    bot.tapHostRoom(hostBot)
    bot.tapReadyCheck()
    bot.tapNext()
    #These bottom three are no longer necessary since tapNext() will continue tapping until leaveRoom()
    #bot.tapUniqueDrop("chardrop")
    #bot.tapRankUp()
    #bot.tapLeaveRoom()

if __name__ ==  '__main__':
    while keyboard.is_pressed("shift+q") != True:
        try:
            problemList = []
            for bot in botList:
                if bot.findParentWindow() == False:
                    bot.openWorldFlipper()
                    problemList.append(bot)
            problemLength = len(problemList)
            if  problemLength > 0:
                sleepTime = 18 + (0.5 * problemLength)
                time.sleep(sleepTime)
                for problem in problemList:
                    problem.checkIfGameOpened()
            for leech in leechList:
                leechCommands(leech)
            hostCommands(hostBot)
            for bot in botList:
                basicCommands(bot)
        except:
            print("oopsie poopsies")
            for bot in botList:
                if bot.findParentWindow() == False:
                    bot.openWorldFlipper()


            

   