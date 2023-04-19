hostName = "WF Alt 1"

def basicCommands(bot):
    bot.findParentWindow()
    ''' These are the optional commands, 
        move them in and out as necessary
        
        
        bot.checkUnitEpisodes()
        
    '''
    bot.tapToStart()
    bot.tapBossFight(True) #Parameter is true when Pickup event
    bot.tapEventButton("eventbutton1")
    
    bot.tapBlueStacksCloseButton()
    bot.tapDialogueYes()
    bot.tapWorldFlipperIcon()
    bot.tapDialogueOk1Error()
    bot.tapDialogueOk2Error()
    bot.tapDialogueAbortError()
    bot.checkConnectionError()

def leechCommands(bot):
    bot.tapHostRoom(hostName,True) #second parameter is True when pickup event is on
    bot.tapReadyCheck()
    bot.tapLeaveRoom(True)
    #bot.tapNext()

def hostCommands(bot):
    if bot.name == "WF Alt 1":
        otherLeech = "WF Alt 2"
    else:
        otherLeech = "WF Alt 1"
    bot.tapBossButton("regi",True) #second parameter is True when pickup event is on
    bot.tapCoop()
    bot.tapRecruit1()
    bot.tapRecruit2()
    #bot.tapStart(otherLeech) #pass in the leechBot because it looks at its name
    bot.exitMatch(10)