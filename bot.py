import os
import discord
from discord.ext import commands
import asyncio
import requests
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#if ROOT_DIR.split("\\")[0] == "C:":
#    root = "http://127.0.0.1:8000/"
#else:
#    root = "http://cryptodala.pythonanywhere.com/"

root = "http://cryptodala.pythonanywhere.com/"

bot = commands.Bot(command_prefix = "!")
TOKEN = "OTUwNjM2MjEzOTE4OTA0MzIw.Yiby9w.iodXiY08j7roYIC2GpbizzyPrCQ"

async def background():
    await bot.wait_until_ready()
    while not bot.is_closed():
        print("loop start")
        await asyncio.sleep(30)
        address = "{}botendpoints/verifications".format(root)
        print(address)
        r = requests.get(address)
        print(r.text)
        data = json.loads(r.text)
        print(data)
        result = "These customers require verification\n"
        
        for j in data:
            id = data[j]["real_id"]
            text = "click to verify: {}botendpoints/verify/{} \n".format(root, id)
            print(text)
            result += text
            
        
        serverr = bot.guilds[0]
        await serverr.text_channels[0].send(result)
        
        

@bot.event
async def on_ready():
    print("{} has  connected to discord".format(bot.user.name))
    serverr = bot.guilds[0]


@bot.event
async def on_member_join(member):
    await member.creat_dm()
    await member.dm_channel.send("welcome {}".format(member.name))

@bot.event
async def on_message(message):
    pass
    #await message.author.create_dm()
    #wait message.author.dm_channel.send("Hello {}".format(message.author.name))
#bot.loop.create_task(background())
bot.run(TOKEN)