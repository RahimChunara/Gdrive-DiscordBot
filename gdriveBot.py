import os
import random
import json
import re
import requests

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'YOUR_DISCORD_KEY'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    flag = 0
    if message.author == client.user:
        return

    args = message.content.split(' ')
    print(args[1])

    
    with open("keys.txt", "a+") as keys:
        keys.seek(0) 
        lines = keys.read().splitlines()
        if args[0] in lines:
        
            url = 'https://gd.zxd.workers.dev/drive'
            myobj = {"teamDriveName":args[2],"teamDriveThemeId":"random","emailAddress":args[1]}
            y = json.dumps(myobj)
            print(y)
            x = requests.post(url, data = y)

            if(x.text):
                response = 'Done check your drive'
                flag = 1
                await message.channel.send(response)
        else: 
            response = 'Key given incorrect or used up maximum times'
            await message.channel.send(response)
    
    if flag == 1:
        with open("keys.txt", "r") as f:
            alllines = f.readlines()
        with open("keys.txt", "w") as f:
            for line in alllines:
                if line.strip("\n") != args[0]:
                    f.write(line)
        flag = 0

client.run(TOKEN)
