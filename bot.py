#!/usr/bin/env python3
import discord
import time
import io
import json
# The class is where the magic happens. You can define functions that happens when something 
# is triggered, like receiving a message
class MyClient(discord.Client):
    lb = open("leaderb.json","r")
    leaderb = json.load(lb)
    lb.close()
    # on_ready happens once when the bot is up and running after boot
    async def on_ready(self):
        print("bot is ready")
        # I use json to store the scores of everyone's nose hits
    # on_message happens after each message is received
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
                if message.author.name in self.leaderb:
                   self.leaderb[message.author.name] += 1
                else:
                    self.leaderb[message.author.name] = 1
                print(self.leaderb)
                lb = open("leaderb.json","w")
                json.dump(self.leaderb,lb)
                lb.close()

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
        if (message.content == "leaderb"):
            s = ""
            for name,score in self.leaderb.items():
                s += name + " a " + str(score) + " points de nez\n"
            await message.reply(s)

# Intents are what you allowed your bot to access when you invited it to a discord server 
# via link. You can change it on the website
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
#I saved the bot key in another file in order to share this without leaking my private key
f = open("discordkey","r")
client.run(f.read())
