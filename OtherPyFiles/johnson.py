import discord
import re
import time
token  = ""
client = discord.Client()  # starts the discord client.


@client.event       
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if "GIVEAWAY" in str(message.content):
        channel = str(message.channel)
        if(channel == '07_staking' or channel == 'rs3_staking' or channel == 'free_bets'):
            if(str(message.author) == "GiveawayBot#2381"):
            	if(len(message.embeds)>0):
                    embedmsg = message.embeds[0].author.name
                    embedmsg = embedmsg.lower()
                    if('test' not in str(embedmsg) and 'tests' not in str(embedmsg) and 'testing' not in str(embedmsg) and 'ban' not in str(embedmsg) and 'banning' not in str(embedmsg) ):
                        fbinmil = " ".join(re.findall("\d+[m,M]",embedmsg))
                        fbnum = " ".join(re.findall("\d+",fbinmil))
                        fbnum = int(fbnum)
                        if(channel == 'rs3_staking' and int(fbnum) >= 5):
                        	time.sleep(3)
                        	await message.add_reaction("🎉")
                        elif(int(fbnum)>=20 and channel == "general"):
                        	time.sleep(3)
                        	await message.add_reaction("🎉")
                        elif(channel == '07_staking'and int(fbnum)>0):
                        	time.sleep(3)
                        	await message.add_reaction("🎉")
                        elif(channel == 'free_bets'):
                            time.sleep(3)
                            await message.add_reaction("🎉")
                        print("==============================================\n")
                        print("Fb amount:",fbnum,"m happening at channel",str(message.channel),"\n")
                            
client.run(token,bot=False)