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


# key = {
#     'r5u7x!A%D*G-KaPd',
# 'WnZr4u7w!z%C*F-J',
# 'eThWmZq4t7w9z$C&',
# 'KbPeShVmYq3t6w9y',
# '*G-KaPdSgVkYp3s6',
# 'z%C*F-JaNdRgUkXp',
# '6w9z$C&F)J@NcRfU',
# 'q3t6v9y$B&E)H@Mc',
# 'VkYp3s6v8y/B?E(H',
# 'dRgUkXp2s5u8x/A?',
# 'J@NcRfUjXn2r5u7x',
# '&E)H@McQfTjWnZr4',
# 'y/B?E(H+MbQeThWm',
# '5u8x/A?D(G+KbPeS',
# 'n2r4u7x!A%D*G-Ka',
# 'TjWnZr4t7w!z%C*F',
# 'bQeThWmZq4t6w9z$',
# 'G+KbPeShVmYq3t6v',
# '%D*G-KaPdSgVkYp3',
# 'w!z%C*F-JaNdRgUk',
# '3t6w9z$C&F)J@NcR',
# 'mYq3s6v9y$B&E)H@',
# 'SgVkYp2s5v8y/B?E',
# 'aNdRgUkXp2r5u8x/',
# 'F)J@NcRfUjXn2r4u',
# '$B&E)H@McQfTjWnZ',
# 'v8y/B?E(H+MbQeTh',
# '2r5u8x/A?D(G+KbP',
# 'jXnZr4u7x!A%D*G-',
# 'QfTjWnZq4t7w!z%C',
# '+MbQeThWmZq3t6w9',
# 'D(G+KbPeShVmYp3s',
# '!A%D*G-KaPdSgVkY',
# 't7w!z%C*F-JaNdRg',
# 'Yq3t6w9z$C&F)J@N',
# 'hVkYp3s6v9y$B&E)',
# 'PdSgVkXp2s5v8y/B',
# '-JaNdRgUkXn2r5u8',
# 'C&F)J@NcRfUjXnZr',
# '9y$B&E)H@McQfTjW',
# 's5v8y/B?E(H+MbQe',
# 'Xn2r5u8x/A?D(G+K',
# 'fUjWnZr4u7x!A%D*',
# 'McQfTjWmZq4t7w!z',
# '(H+MbQeThVmYq3t6',
# 'A?D(G+KbPeShVkYp',
# '7x!A%D*G-KaPdSgV',
# 'q4t7w!z%C*F-JaNd',
# 'VmYq3t6w9z$C&F)J',
# 'eSgVkYp3s6v9y$B&',
# 'KaPdSgUkXp2s5v8y',
# '*F-JaNdRgUjXn2r5',
# 'z$C&F)J@NcRfTjWn',
# '6v9y$B&E)H@McQfT',
# 'p2s5v8y/B?E(H+Mb',
# 'UjXn2r5u8x/A?D(G',
# 'cRfTjWnZr4u7x!A%',
# 'H@McQeThWmZq4t7w',
# '?E(H+MbQeShVmYq3',
# 'x/A?D(G+KbPeSgVk',
# '4u7x!A%D*G-KaPdS',
# 'mZq4t7w!z%C*F-Ja',
# 'ShVmYq3t6w9z$C&F',
# 'bPdSgVkYp3s6v9y$',
# 'G-KaPdRgUkXp2s5v',
# '%C*F-JaNcRfUjXn2',
# 'w9z$C&F)J@NcQfTj',
# '3s6v9y$B&E)H@McQ',
# 'kXp2s5v8y/B?E(H+',
# 'RfUjXn2r5u8x/A?D',
# '@McQfTjWnZr4u7x!',
# 'E)H@MbQeThWmZq4t',
# '/B?E(H+MbPeShVmY',
# 'u8x/A?D(G+KbPdSg',
# 'Zr4u7x!A%D*G-KaN',
# 'hWmZq4t7w!z%C*F-',
# 'PeShVmYq3t6w9z$C',
# '+KaPdSgVkYp3s6v9',
# 'D*G-JaNdRgUkXp2s',
# '!z%C*F-J@NcRfUjX',
# 't6w9z$C&F)J@McQf',
# 'Yp3s6v9y$B&E)H@M',
# 'gUkXp2s5v8y/B?E(',
# 'NcRfUjXn2r5u8x/A',
# ')H@McQfTjWnZr4u7',
# 'B&E)H+MbQeThWmZq',
# '8y/B?E(H+KbPeShV',
# 'r5u8x/A?D(G-KaPd',
# 'WnZr4u7x!A%D*G-J',
# 'eThWmZq4t7w!z%C*',
# 'KbPeShVmYq3t6w9z',
# '*G-KaPdSgVkYp3s6',
# 'A%D*F-JaNdRgUkXp',
# '7w!z%C*F)J@NcRfU',
# 'q3t6w9z$C&F)H@Mc',
# 'VkYp3s6v9y$B&E(H',
# 'dRgUkXp2s5v8y/B?',
# 'J@NcRfUjXn2r5u8x',
# '&E)H@McQfTjWnZr4',
# 'y$B&E(H+MbQeThWm',

# }



client.run(TOKEN)
