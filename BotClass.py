from ctypes.wintypes import HWND
from faulthandler import cancel_dump_traceback_later
import pyautogui
from pyautogui import *
import time
import os
import win32api, win32con, win32gui

class Bot:
    checktimer = 0
    gameopencheck = 0
    def __init__(self,name,x,y):
        self.name = name
        self.changeOrigin(x,y)
        self.changeOffsets(0,0)
    def changeOffsets(self,x,y):
        self.xOff = x
        self.yOff = y
    def getOffsets(self):
        return self.xOff,self.yOff
    def changeOrigin(self,x,y):
        self.xOrigin = x
        self.yOrigin = y
    def getOrigin(self):
        return self.xOrigin,self.yOrigin
    
    def LocateImageCenter(self,pic,x1,x2,x3,x4,gs,conf):
        return pyautogui.locateCenterOnScreen("C:\\Users\\lucac\\Documents\\Coding\\Python\\WorldFlipperBot\\Images\\%s.png" % (pic),region=(x1,x2,x3,x4),grayscale = gs,confidence = conf)
    def LocateImageCenterAnywhere(self,pic,gs,conf):
        return pyautogui.locateCenterOnScreen("C:\\Users\\lucac\\Documents\\Coding\\Python\\WorldFlipperBot\\Images\\%s.png" %(pic),grayscale = gs,confidence = conf)
    def LocateImageCorner(self,pic,x1,x2,x3,x4,gs,conf):
        return pyautogui.locateOnScreen("C:\\Users\\lucac\\Documents\\Coding\\Python\\WorldFlipperBot\\Images\\%s.png" % (pic),region=(x1,x2,x3,x4),grayscale = gs,confidence = conf)
    def LocateImageCornerAnywhere(self,pic,gs,conf):
        return pyautogui.locateOnScreen("C:\\Users\\lucac\\Documents\\Coding\\Python\\WorldFlipperBot\\Images\\%s.png" %(pic),grayscale = gs,confidence = conf)

    def click(self,target, timeToSleep = 0):
        win32api.SetCursorPos((target.x,target.y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        if time.sleep != 0:
            time.sleep(timeToSleep)  
    
    def scroll(self, direction = "down",target = "center"):
        try:
            if target == "center":
                scrollX = int((self.xOrigin+self.xOff)+(563/2))
                scrollY  = int((self.yOrigin+self.yOff)+(974/2))
            else:
                scrollX = int(target.x)
                scrollY = int(target.y)
            win32api.SetCursorPos((scrollX,scrollY))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.5)
            if direction == "down":
                for x in range(200):
                    win32api.SetCursorPos((scrollX,scrollY-x))
                    time.sleep(0.001)
            elif direction == "up":
                for x in range(200):
                    win32api.SetCursorPos((scrollX,scrollY+x))
                    time.sleep(0.001)
            elif direction == "left":
                for x in range(200):
                    win32api.SetCursorPos((scrollX+x,scrollY))
                    time.sleep(0.001)
            elif direction == "right":
                for x in range(200):
                    win32api.SetCursorPos((scrollX-x,scrollY))
                    time.sleep(0.001)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) 
           
        except Exception as e:
            print("Scrolling failed lol")
            print (e)

        
          
    def list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
        win32gui.EnumWindows(winEnumHandler, None)
    def get_inner_windows(self,whndl,subprocess):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd) or subprocess == 2:
                hwnds[win32gui.GetClassName(hwnd)] = hwnd
            return True
        hwnds = {}
        win32gui.EnumChildWindows(whndl, callback, hwnds)
        return hwnds
    def getWindowCoords(self):
        hwnd = win32gui.FindWindow(None, self.name)
    def bringToFront(self):
        hwnd = win32gui.FindWindow(None, self.name)

        try:
            x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
            w = 540
            h = 960
            xdiff = x1-x0
            ydiff = y1-y0
            if xdiff != w or ydiff != h:
                win32gui.MoveWindow(hwnd,x0,y0,w,h,True)
                win32gui.UpdateWindow(hwnd)
        except Exception as e:
            print("Could not resize window to default size")
            print(e)
        try:
            #wInt = 0 #starting process is 0, sub-process will be 1, etc...
            #hwnd = self.get_inner_windows(hwnd,wInt)['RenderWindow']
            win32gui.SetForegroundWindow(hwnd)
            return True
        except Exception as e:
            print("Could not set " + self.name + " as the foreground window.")
            print(e)
            return False
    def openWorldFlipper(self,timeBetweenOpen = 0.5):
        name = self.name
        os.startfile("C:\\Users\\lucac\\Documents\\Coding\\Python\\WorldFlipperBot\\open "+name)
        time.sleep(timeBetweenOpen)
        time.sleep(20)
        self.checkIfGameOpened()
        print(self.findParentWindow())

    def tapWorldFlipperIcon(self):
        x1 = self.xOrigin+self.xOff + 300
        y1 = self.yOrigin+self.yOff + 200
        x2 = 200
        y2 = 200
        wficon = self.LocateImageCenter("worldflippericon",x1,y1,x2,y2,True,0.8)
        if wficon != None:
            click(wficon)
            time.sleep(20)
            self.checkIfGameOpened()


    def checkIfGameOpened(self):
        self.findParentWindow()
        startButtonOnScreen = self.tapToStart(False)
        while startButtonOnScreen != True:
            self.closeWorldFlipper()
            time.sleep(1)
            self.openWorldFlipper()
            time.sleep(20)
            startButtonOnScreen = self.tapToStart(False)
        self.tapToStart(True)

    def closeWorldFlipper(self):
        name = self.name
        try:
            hwndTop = win32gui.FindWindow(None, name)
            win32gui.PostMessage(hwndTop,win32con.WM_CLOSE,0,0)
            closed = self.tapBlueStacksCloseButton()
            while closed != True:
                closed = self.tapBlueStacksCloseButton()
        except Exception as e:
            print(e)
            self.openWorldFlipper(True)

    def screenshotRegion(self,x1,y1,x2,y2):
        iml = pyautogui.screenshot(region=(x1,y1,x2,y2))
        iml.save(r"C:\\Users\\lucac\Documents\\Coding\\Python\savedimage.png")

    def findParentWindow(self):
        parentWindow = self.LocateImageCorner(self.name,self.xOrigin+self.xOff,self.yOrigin+self.yOff,95,40,True,0.95)

        if (parentWindow == None):
            self.checktimer+=1
            if (self.bringToFront() == True):
                print("Do something")
            
        parentWindow = self.LocateImageCornerAnywhere(self.name,True,0.98)
        try:
            self.xOff = parentWindow.left - self.xOrigin
            self.yOff = parentWindow.top - self.yOrigin
            self.checktimer = 0
            return True
        except:
            print('Cannot see %s Window! Please move the window into view, fully unobstructed.' % (self.name))
            if self.checktimer > 3:
                return False
            else:
                return True

    
    def tapBlueStacksCloseButton(self):
        x1 = self.xOrigin+self.xOff+120
        y1 = self.yOrigin+self.yOff+450
        x2 = 340
        y2 = 100
        closebutton = self.LocateImageCenter("closeBluestacksWindow",x1,y1,x2,y2,False,0.8)
        if closebutton != None:
            click(closebutton)
            return True
        return False

    def tapToStart(self,canClick = True):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 375
        x2 = 125
        y2 = 125
        taptostart = self.LocateImageCenter("taptostart",x1,y1,x2,y2,True,0.65)
        if taptostart != None:
            if canClick:
                for x in range(5):
                    self.click(taptostart)
            return True
        else:
            return False
    def tapBossFight(self,pickup=False):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 780
        x2 = 540
        y2 = 120
        if pickup == True:
            bossfight = self.LocateImageCenter("bossfightPU",x1,y1,x2,y2,True,0.9)
        else:
            self.screenshotRegion(x1,y1,x2,y2)
            bossfight = self.LocateImageCenter("bossfight",x1,y1,x2,y2,True,0.9)
        if bossfight != None:
            self.click(bossfight,1)

    def tapEventButton(self,eventname):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 200
        x2 = 540
        y2 = 425
        eventButton = self.LocateImageCenter(eventname,x1,y1,x2,y2,True,0.90)
        
        if eventButton != None:
            self.click(eventButton)
    
    def tapDialogueOk1Error(self):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff
        x2 = 565
        y2 = 980
        okerror = self.LocateImageCenter("okerror",x1,y1,x2,y2,True,0.85)
        if okerror != None:
            self.click(okerror)
            return True
        return False
    def tapDialogueOk2Error(self):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 300
        x2 = 540
        y2 = 400
        okerror2 = self.LocateImageCenter("okerror2",x1,y1,x2,y2,True,0.95)
        if okerror2 != None:
            self.click(okerror2)
    def tapDialogueAbortError(self):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 300
        x2 = 540
        y2 = 400
        aborterror = self.LocateImageCenter("aborterror",x1,y1,x2,y2,True,0.95)
        if aborterror != None:
            self.click(aborterror)
    def tapDialogueYes(self):
        x1 = self.xOrigin+self.xOff
        y1 = self.yOrigin+self.yOff + 600
        x2 = 540
        y2 = 100
        abort2 = self.LocateImageCenter("abort2",x1,y1,x2,y2,True,0.75)
        if abort2 != None:
            self.click(abort2)
    def checkConnectionError(self):
        x1 = self.xOrigin+self.xOff + 75
        y1 = self.yOrigin+self.yOff + 400
        x2 = 300
        y2 = 150
        
        networkConnectionError = self.LocateImageCenter("connectionError",x1,y1,x2,y2,True,0.75)
        if networkConnectionError != None:
            self.checkIfGameOpened()
            return True
        return False

    def checkAllErrors(self):
        self.checkConnectionError()
        self.tapDialogueAbortError()
        self.tapDialogueOk1Error()
        self.tapDialogueOk2Error()
        self.tapDialogueYes()

    def checkUnitEpisodes(self):
        def checkSkipButton():
            x1 = self.xOrigin+self.xOff + 400
            y1 = self.yOrigin+self.yOff + 25
            x2 = 130
            y2 = 75
        
            skipButton = self.LocateImageCenter("unitepisodeskip",x1,y1,x2,y2,True,0.8)
            if skipButton!= None:
                self.click(skipButton,0.5)
                return True
            return False
        def checkProceed():
            x1 = self.xOrigin+self.xOff + 200
            y1 = self.yOrigin+self.yOff
            x2 = 275
            y2 = 900
        
            proceedButton = self.LocateImageCenter("unitepisodeproceed",x1,y1,x2,y2,True,0.8)
            if proceedButton != None:
                self.click(proceedButton,1)
                return True
            return False
        def checkClose():
            x1 = self.xOrigin+self.xOff + 200
            y1 = self.yOrigin+self.yOff + 550
            x2 = 275
            y2 = 200
        
            closeButton = self.LocateImageCenter("unitepisodeclose",x1,y1,x2,y2,True,0.8)
            if closeButton != None:
                self.click(closeButton)
                return True
            return False

        def checkNewStory(clickButton = True):
            x1 = self.xOrigin+self.xOff 
            y1 = self.yOrigin+self.yOff + 200
            x2 = 100
            y2 = 750

            newStory = self.LocateImageCenter("unitepisodenew",x1,y1,x2,y2,False,0.9)
            if newStory != None:
                if clickButton == True:
                    self.click(newStory,0.3)
                return True
            return False
        def checkReturn():
            x1 = self.xOrigin+self.xOff 
            y1 = self.yOrigin+self.yOff + 900
            x2 = 100
            y2 = 50
            
            returnButton = self.LocateImageCenter("unitepisodereturn",x1,y1,x2,y2,True,0.95)
            newStory = checkNewStory(False)
            if returnButton != None and newStory == False:
                self.click(returnButton)
                return True
            return False
        def checkYesAnywhere():
            yesButton = self.LocateImageCenterAnywhere("abort2",False,0.95)
            if yesButton != None:
                self.click(yesButton)
                return True
            return False
        checkNewStory()
        checkYesAnywhere()
        checkSkipButton()
        checkProceed()
        checkClose()
        checkReturn()


    

    