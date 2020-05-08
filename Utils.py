import discord
import Constants
import random
from twilio.rest import Client



# Method to create an instance of discord
def createInstanceOfDiscord(token):
    return discord.Client()
    
def callMyPhone():
    client = Client(Constants.account_sid, Constants.auth_token)
    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='',
                        from_=''
                    )
    print(call.sid)

def getMessageIfWin():
    return Constants.REPLYLIST[random.randint(0,len(Constants.REPLYLIST)-1)]

def getGoodLuck():
    return Constants.GOODLUCKLIST[random.randint(0,len(Constants.GOODLUCKLIST)-1)]
    

def getMessageIfRebetOrCollect():
    return Constants.COLLECTOREBETLIST[random.randint(0,len(Constants.COLLECTOREBETLIST)-1)]


def getRandomMessage():
    return Constants.RANDOMLIST[random.randint(0,len(Constants.RANDOMLIST)-1)]
