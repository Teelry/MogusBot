#!/usr/bin/env python3
import discord
import time
import io

#The class is where the magic happens. You can define functions that happens when something 
#is triggered, like receiving a message
class MyClient(discord.Client):
    #on_ready happens once when the bot is up and running after boot
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    #
    async def on_message(self, message):
        print(message.author)
        t = time.localtime()
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        if (message.content == "nez"):
            if (h-m == 0):
                await message.add_reaction("👃")
                await message.add_reaction("✔️")
                await message.reply("Félicitations ! Tu gagnes 1 point de :nose:")

            if (h-m == 1):
                await message.add_reaction("👃")
                await message.add_reaction("❌")
                await message.reply("Presque mais trop tôt !")
            if (h-m == -1):
                await message.add_reaction("👃")
                await message.add_reaction("❌")
                await message.reply("Trop tard :rofl: :call_me:")
            else:
                await message.add_reaction("👃")
                await message.add_reaction("❌")
                await message.reply("T'es complètement bourré ou quoi? :rofl: :call_me:")
        if (message.content == "nezsec"):
            d = str(60-s)
            await message.reply("Il reste "+d+" secondes avant la prochaine minute")
#Intents are what you allowed your bot to access when you invited it to a discord server via link. You can change it on the website
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
#I saved the bot key in another file in order to share this without leaking my private key
f = open("discordkey","r")
client.run(f.read())
