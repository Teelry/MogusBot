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
    last = time.localtime()
    lastday = last.tm_mday
    lastmonth =last.tm_mon
    lasthour = last.tm_hour
    lastmin = last.tm_min
    # on_ready happens once when the bot is up and running after boot
    async def on_ready(self):
        print("bot is ready")
        # I use json to store the scores of everyone's nose hits
    # on_message happens after each message is received
    async def on_message(self, message):
        
        t = time.localtime()
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        ms = int(time.time() * 1000) % 1000
        day = t.tm_mday
        month = t.tm_mon

        if (message.content == "nez"):
            if (day == self.lastday and month == self.lastmonth and h == self.lasthour and m == self.lastmin):
                await message.add_reaction("👃")
                await message.add_reaction("❌")
                await message.reply("Aie aie aie quelqu'un t'a volé tes zapatos :sob:")
                h += 1

            if (h-m == 0):
                mult = 1
                points = 1
                s = ""
                if (ms <= 42 and message.author.name != "César"):
                    s = "Bonus ! " + str(ms) + " milisecondes "
                    mult = 10
                    await message.add_reaction("🥳")
                
                if (h == 11 or h == 22 or h == 0):
                    points = 2

                await message.add_reaction("👃")
                await message.add_reaction("✔️")
                await message.reply(s +"Félicitations ! Tu gagnes "+ str(mult * points) +" point de :nose:")
               
                if message.author.name in self.leaderb:
                    self.leaderb[message.author.name] += mult * points
                else:
                    self.leaderb[message.author.name] = mult * points
              
                self.lastday = day
                self.lastmonth = month

                lb = open("leaderb.json","w")
                json.dump(self.leaderb,lb)
                lb.close()

            if (h-m == 1):
                await message.add_reaction("👃")
                await message.add_reaction("❌")
                await message.reply("Presque mais trop tôt ! -1 !")
                if message.author.name in self.leaderb:
                    self.leaderb[message.author.name] -= - 1
                else:
                    self.leaderb[message.author.name] = -1
                lb = open("leaderb.json","w")
                json.dump(self.leaderb,lb)
                lb.close()

            if (h-m == -1):
                await message.add_reaction("👃")
                await message.add_reaction("❌")
                await message.reply("Trop tard :rofl: :call_me:")

            if (h-m > 1 or h-m < -1):
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
