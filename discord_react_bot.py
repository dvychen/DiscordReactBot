import discord


from dotenv import load_dotenv

import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(os.getenv("MESSAGE"))
        await message.channel.send(os.getenv("MESSAGE_TWO"))

client.run(os.getenv("DISCORD_TOKEN"))