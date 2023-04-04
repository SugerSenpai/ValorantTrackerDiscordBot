import discord
from responses import handleResponses

botToken = "YOUR TOKEN"

async def sendMessage(message, userMessage):
    try:
        response = handleResponses(userMessage)
        await message.channel.send(response)
    except Exception as e:
        print(e)

async def sendPicture(message, userMessage):
    try:
        response = handleResponses(userMessage)
        await message.channel.send(file = discord.File(response +".png"))
    except Exception as e:
        print(e)
    
def runDicsordBot():
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        userMessage = str(message.content)
        userName = str(message.author)
        if userMessage[0:8] == "!refresh":
            await sendMessage(message, userMessage)
        if userMessage[0:8] == "!tracker":
            await sendPicture(message, userMessage)
            await message.channel.send("Here is your tracker score @" + userName)
    client.run(botToken)