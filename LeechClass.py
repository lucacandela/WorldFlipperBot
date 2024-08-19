from BotClass import Bot
import time
class LeechBot(Bot):
    def tapHostRoom(self,hostName,pickup=False):
        def findHostRoom():
            x1 = self.xOrigin+self.xOff + 100
            y1 = self.yOrigin+self.yOff
            x2 = 300
            y2 = 900
            if hostName == "WF Alt 1":
                hostroomname = "host2lobby"
            else:
                hostroomname = "host3lobby"
            if pickup == True:
                return self.LocateImageCenter(hostroomname+"PU",x1,y1,x2,y2,False,0.85)
            else:
                return self.LocateImageCenter(hostroomname,x1,y1,x2,y2,False,0.98)
        
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 200
        x2 = 540
        y2 = 525
        bosslist = self.LocateImageCenter("bosslist",x1,y1,x2,y2,True,0.85)
        if bosslist != None:
            time.sleep(1.2)
            hostroom =  findHostRoom()
            if hostroom != None:
                hostroom = findHostRoom()
                if hostroom != None:
                    self.click(hostroom,0)
                    if self.roomStartedError() != True:
                        print ("Host Room was entered successfully")
                    else:
                        print ("Host Room had a starting error, but it was resolved")
            else:
                self.tapRefreshButton(True)
                time.sleep(1)
                hostroom = findHostRoom()
                if hostroom != None:
                    self.click(hostroom,0)
                    if self.roomStartedError() != True:
                        print ("Host Room was entered successfully")
                    else:
                        print ("Host Room had a starting error, but it was resolved")
    def tapRefreshButton(self,checkTime = True):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 200
        x2 = 540
        y2 = 525
        bosslist = self.LocateImageCenter("bosslist",x1,y1,x2,y2,True,0.85)
        if bosslist != None:
            refreshbutton = self.LocateImageCenter("refreshbutton",x1,y1-100,x2,y2,True,0.85)
            if refreshbutton != None and (self.checktimer % 2 == 0) or (checkTime == False):
                time.sleep(5)
                self.click(refreshbutton)
                return True
        return False
    def roomStartedError(self):
        x1 = self.xOrigin+self.xOff + 75
        y1 = self.yOrigin+self.yOff + 400
        x2 = 300
        y2 = 150
        
        roomStarted = self.LocateImageCenter("roomstartederror",x1,y1,x2,y2,True,0.75)
        if roomStarted != None:
            okButtonPresent = self.tapDialogueOk1Error()
            while okButtonPresent != True:
                okButtonPresent = self.tapDialogueOk1Error
            time.sleep(0.5)
            refreshPressed = self.tapRefreshButton(False)
            while refreshPressed != True:
                refreshPressed = self.tapRefreshButton(False)

        return False
    def tapReadyCheck(self):
        x1 = self.xOrigin+self.xOff + 153
        y1 = self.yOrigin + self.yOff + 680
        x2 = 75
        y2 = 75

        readycheck = self.LocateImageCenter("readycheck",x1,y1,x2,y2,True,0.75)
        if readycheck != None:
            self.click(readycheck,0.1)
    
    def tapNext(self):
        x1 = self.xOrigin+self.xOff + 173
        y1 = self.yOrigin + self.yOff + 890
        x2 = 190
        y2 = 65

        next = self.LocateImageCenter("next",x1,y1,x2,y2,True,0.65)
        if next != None:
            leaveRoomVisible = self.tapLeaveRoom()
            while leaveRoomVisible != True:
                self.click(next)
                time.sleep(0.2)
                leaveRoomVisible = self.tapLeaveRoom()
            if leaveRoomVisible == True:
                self.tapLeaveRoom(True)
                
            

        
    def tapUniqueDrop(self,dropname):
        x1 = self.xOrigin+self.xOff + 83
        y1 = self.yOrigin + self.yOff + 400
        x2 = 250
        y2 = 580
        uniquedrop = self.LocateImageCenter(dropname,x1,y1,x2,y2,True,0.90)
        if uniquedrop != None:
            self.click(uniquedrop)

    
    def tapLeaveRoom(self,canClick = False):
        x1 = self.xOrigin+self.xOff + 88
        y1 = self.yOrigin + self.yOff + 900
        x2 = 145
        y2 = 40
        leavequest = self.LocateImageCenter("leavequest",x1,y1,x2,y2,True,0.7)
        if leavequest != None:
            if canClick == True:
                self.click(leavequest)
            else:
                return True
        else:
            return False

    
    def tapRankUp(self):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin + self.yOff
        x2 = 565
        y2 = 980
        rankedup = self.LocateImageCenter("rankedup",x1,y1,x2,y2,True,0.90)
        if rankedup != None:
            self.click(rankedup)


