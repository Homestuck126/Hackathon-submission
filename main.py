import discord
import os
from discord.ext import commands
import requests
import json

secret = os.environ['Token']

client = commands.Bot(command_prefix = "$")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Working"))
    print("Moderation Bot Online and Running")

@client.event
async def on_message(message):
  msg = message.content

  if message.author == client.user:
    return
  if msg.startswith('$hi'):
    await message.channel.send('Hello!')

client.run(secret)

