import discord
import re
import time
import random
token  = ""
client = discord.Client()  # starts the discord client.
temp = 'randomtext'
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    msg = str(message.content).lower()
    print(client.user in message.mentions)
    for user in message.mentions:
        print(user.name)
    rebet = "rebet"
    collect = "collect"
    reply = ["reeeee","ez","lets go","hehe","nice","haha","lol"]
    collectorrebet = [collect,"wallet pls","wallet me bro","rebet","wallet","i will collect"]
    if(client.user in message.mentions):
        if(rebet in msg or collect in msg):
            time.sleep(3)
            await message.channel.send(collectorrebet[random.randint(0,len(collectorrebet)-1)])
        elif("won" in msg):
            time.sleep(3)
            await message.channel.send(reply[random.randint(0,len(reply)-1)])
    # arrayofmsgs = [':dog:',':pig_nose:','Kill him',":rolling_eyes:",'goodluck','GoodLuck','glglgl','gl','ez','cmon','goodluck guys','atb',':nerd:',':eggplant:',':100:',':poop:',':money_mouth:',':frowning:',':detective:',':cherries:','Easy','fsfdfd',':lollipop:']
    arrayofmsgs = ['goodluck','GoodLuck','glglgl','gl','glgl','gl gl','Good Luck','!gl','good luck','gl g']
    
    temp = ""
    if "pot" in msg and temp != msg:
        temp = msg
        fbinmil = " ".join(re.findall("\d+[m,M]",msg))
        fbnum = " ".join(re.findall("\d+",fbinmil))
        fbnum = int(fbnum)
        if(fbnum >= 100):
            channel = str(message.channel)
            if(channel == '07_staking'):
                if(str(discord.utils.get(message.author.roles, name="Host")) == 'Host' or str(discord.utils.get(message.author.roles, name="Admin")) == 'Admin'):
                    ra = random.randint(0,len(arrayofmsgs)-1)
                    print(message.author,message.channel,ra)
                    time.sleep(5)
                    content = "{0}".format(arrayofmsgs[ra])
                    await message.channel.send(content)

    # elif 
client.run(token,bot=False)