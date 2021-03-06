# importing required libraries
import discord
import re
import time
import random
from Utils import *
import Constants


# Creating a instance of discord
client = createInstanceOfDiscord(Constants.token_for_warnerjeton)

# This event gets executed when the client is logged in.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# This event listener will be triggered on every message.
@client.event
async def on_message(message):
    messageObj = message
    message: str = str(message.content).lower()
    channelName: str = str(messageObj.channel)
    authorName: str = str(messageObj.author)
    serverName: str = str(messageObj.guild.name)

    # Giveaway code starts here.
    # Checking whether giveway is present in the message
    if Constants.GIVEAWAY in message and serverName == Constants.TESTSERVER:
        # Checking whether the message is from particular channel
        if( channelName == Constants.OLDSCHOOLSTAKING or channelName ==  Constants.RS3STAKING or channelName == Constants.FREEBETS ):
            # Checking the author name
            if(authorName == Constants.GIVEAWAYBOTID):
                # checking if the length of embeds is greater than 0
                if(len(messageObj.embeds)>0):
                    #  Getting the embed message
                    embedmsg:str = messageObj.embeds[0].author.name
                    embedmsg:str = embedmsg.lower()

                    # Checking whether the giveaway is for testing purpose if not it will go.
                    if('test' not in str(embedmsg) and 'tests' not in str(embedmsg) and 'testing' not in str(embedmsg) and 'ban' not in str(embedmsg) and 'banning' not in str(embedmsg) ):
                        #  Regex for getting the amount of free bet.
                        print(embedmsg)
                        fbinmil:str = " ".join(re.findall("\d+[m,M]",embedmsg))
                        print(fbinmil)
                        fbnum:str = " ".join(re.findall("\d+",fbinmil))
                        fbnum:int = int(fbnum)
                        fbFlag = 0
                        if(channelName == Constants.RS3STAKING and int(fbnum) >= 10):
                            time.sleep(6)
                            if "say" in embedmsg:
                                await messageObj.channel.send(getGoodLuck())
                            await messageObj.add_reaction(Constants.REACTMESSAGE)
                        elif(int(fbnum)>=20 and channelName == Constants.GENERAL):
                            time.sleep(6)
                            if "say" in embedmsg:
                                await messageObj.channel.send(getGoodLuck())
                            await messageObj.add_reaction(Constants.REACTMESSAGE)
                        elif(channelName == Constants.OLDSCHOOLSTAKING and int(fbnum)>0):
                            time.sleep(6)
                            if "say" in embedmsg:
                                await messageObj.channel.send(getGoodLuck())
                            await messageObj.add_reaction(Constants.REACTMESSAGE)
                        elif(channelName == Constants.FREEBETS):
                            time.sleep(6)
                            await messageObj.add_reaction(Constants.REACTMESSAGE)
                        print(Constants.LINEBREAKS)
                        print("Fb amount:",fbnum,"m happening at channel",str(messageObj.channel),"\n")

    # Sending auto message if a giveaway is won.
    if(client.user in messageObj.mentions):
        callMyPhone()
        if(Constants.REBET in message or Constants.COLLECT in message):
            time.sleep(2)
            await messageObj.channel.send(getMessageIfRebetOrCollect())
        elif("current" in message):
            time.sleep(2)
            await messageObj.channel.send("gl")





client.run(Constants.token_for_warnerjeton,bot=False)