from telnetlib import X3PAD
from unittest import skip
from BotClass import Bot   
import time

class HostBot(Bot):
    recruitButtonClicked = False
    def tapCoop(self):
        x1 = self.xOrigin+self.xOff + 0 
        y1 = self.yOrigin+self.yOff + 517
        x2 = 540
        y2 = 300
        coop = self.LocateImageCenter("coop",x1,y1,x2,y2,True,0.65)
        if coop != None:
            self.click(coop)
            self.recruitButtonClicked = False
    def tapRecruit1(self):
        x1 = self.xOrigin+self.xOff + 0
        y1 = self.yOrigin+self.yOff + 567
        x2 = 540
        y2 = 170
        recruit = self.LocateImageCenter("recruit",x1,y1,x2,y2,False,0.90)
        if recruit != None and self.recruitButtonClicked == False:
            self.click(recruit,0.4)
            self.recruitButtonClicked = True
            
            
    def tapRecruit2(self):
        x1 = self.xOrigin+self.xOff + 0
        y1 = self.yOrigin+self.yOff + 567
        x2 = 540
        y2 = 185
        recruit2 = self.LocateImageCenter("recruit2",x1,y1,x2,y2,True,0.8)
        #self.screenshotRegion(x1,y1,x2,y2)
        if recruit2 != None:
            self.click(recruit2)

    #Will tap start if 
    def tapStart(self,otherLeech):
        x1 = self.xOrigin+self.xOff + 0
        y1 = self.yOrigin+self.yOff + 567
        x2 = 540
        y2 = 170
        #self.screenshotRegion(x1,y1,x2,y2)
        start = self.LocateImageCenter("start",x1,y1,x2,y2,False,0.85)
        if start != None:
            x3 = self.xOrigin+self.xOff + 162
            y3 = self.yOrigin+self.yOff + 267
            x4 = 350
            y4 = 75
            if otherLeech == "WF Alt 1":
                leech2 = self.LocateImageCenter("leechname2",x3,y3,x4,y4,True,0.85)
            else:
                leech2 = self.LocateImageCenter("leechname3",x3,y3,x4,y4,True,0.85)
            leech1 = self.LocateImageCenter("leechname1",x3,y3,x4,y4,True,0.85) #Main character "Link" will always be leech1
            start = self.LocateImageCenter("start",x1,y1,x2,y2,False,0.85)
            if leech1 != None and leech2 != None and start != None:
                self.click(start)

    def tapStartOnly2P(self):
        x1 = self.xOrigin+self.xOff + 0
        y1 = self.yOrigin+self.yOff + 580
        x2 = 540
        y2 = 170
        start = self.LocateImageCenter("start",x1,y1,x2,y2,False,0.85)
        #self.screenshotRegion(x1,y1,x2,y2)
        if start != None:
            x3 = self.xOrigin+self.xOff + 162
            y3 = self.yOrigin+self.yOff + 267
            x4 = 350
            y4 = 75
            leech1 = self.LocateImageCenter("leechname1",x3,y3,x4,y4,True,0.85) #Main character "Link" will always be leech1
            start = self.LocateImageCenter("start",x1,y1,x2,y2,False,0.85)
            if leech1 != None and start != None:
                self.click(start)
                self.recruitButtonClicked = False
    
    def exitMatch(self,pauseTime):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 10
        x2 = 80
        y2 = 120
        x3 = 540
        y3 = 457
        pause = self.LocateImageCenter("pause",x1,y1,x2,y2,True,0.75)
        try:
            if pause != None:
                time.sleep(pauseTime)
                self.click(pause,1)

        except:
            print("Unkown 'pause' error")
        abort = self.LocateImageCenter("abort",x1,y2+600,x3,y3+200,True,0.93)
        self.screenshotRegion(x1,y2+600,x3,y3+300)
        if abort != None:
            pauseTime += 0.3
            self.click(abort,0.5)

        abort2 = self.LocateImageCenter("abort2",x1,y2+650,x3,150,True,0.75)
        #self.screenshotRegion(x1,y2+650,x3,150)
        if abort2 != None:
            self.click(abort2)

    def lookForBossRoom(self, name, skipCheck = False):
        x1 = self.xOrigin + self.xOff
        y1 = self.yOrigin + self.yOff
        x2 = 540
        y2 = 957
        #bosslist coords
        x3 = self.xOrigin+self.xOff
        y3 = self.yOrigin+self.yOff + 200
        x4 = 540
        y4 = 525
        #checks to see if you're on the boss screen
        #self.screenshotRegion(x3,y3,x4,y4)
        bosslist = self.LocateImageCenter("bosslist",x3,y3,x4,y4,False,0.98)
        #self.screenshotRegion(x3,y3,x4,y4)
        itemexchange = self.LocateImageCenter("itemexchange1",x3,y3,x4,y4,True,0.85)
        if itemexchange == None:
            itemexchange = self.LocateImageCenter("itemexchange2",x3,y3,x4,y4,True,0.85)
        if bosslist != None or itemexchange != None or skipCheck:
            boss = self.LocateImageCenter(name,x1,y1,x2,y2,True,0.7)
            if name == "event1" or name == "event2":
                self.tapEventButton("eventbutton1")
                time.sleep(2.5)
            if boss != None:
                self.click(boss,3.5)
            else:
                self.scroll("down")
                self.lookForBossRoom(name,True)
            


    def tapBossButton(self,name, rateup = False):
        if rateup:
            newName = name + "UP"
        else:
            newName = name
        if name == "orochi":
            name = "orochi"
            self.lookForBossRoom(newName + "1")
            self.lookForBossRoom(name + "2")
        elif name == "regi" or name == "regitare":
            name = "regi"
            self.lookForBossRoom(newName + "1")
            self.lookForBossRoom(name + "2")
        elif name == "golem" or name == "golex":
            name = "golem"
            self.lookForBossRoom(newName + "1")
            self.lookForBossRoom(name + "2")
        elif name == "crab" or name == "hermit":
            name = "crab"
            self.lookForBossRoom(newName + "1")
            self.lookForBossRoom(name + "2")
        elif name == "demon":
            name = "demon"
            self.lookForBossRoom(newName + "1")
            self.lookForBossRoom(name + "2")
        elif name == "whitetail":
            name = "whitetail"
            self.lookForBossRoom(newName + "1")
            self.lookForBossRoom(name + "2")
        elif name == "bear":
            name = "bear"
            self.lookForBossRoom(newName+ "1")
            self.lookForBossRoom(name+ "2")
        elif name == "admin" or name =="administrator":
            name = "admin"
            self.lookForBossRoom(newName+"1")
            self.lookForBossRoom(name + "2")
        elif name == "event1":
            self.lookForBossRoom(name)
        elif name == "event2":
            self.lookForBossRoom(name)


        

    #exitMatch(1)