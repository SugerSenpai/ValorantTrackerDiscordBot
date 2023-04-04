import discord
import tracker

def handleResponses(message: str) -> str:
    message = message.lower()
    if message[0:8] == "!tracker":
        valoName, valoTag = message[9:len(message)].split("#")
        tracker.getTrackerScore(valoName,valoTag)
        return(valoName+valoTag)
    if message[0:8] == "!refresh":
        valoName, valoTag = message[9:len(message)].split("#")
        tracker.refreshTrackerScore(valoName,valoTag)
        return("Your Tracker was successfully refreshed")
    else:
        return "use !refresh name#tag or !tracker name#tag to use me"