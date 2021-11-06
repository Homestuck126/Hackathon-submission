import discord
import os
from discord.ext import commands
from replit import db
import random
import map
secret = os.environ['Token']

client = commands.Bot(command_prefix = "$")

db["cult"]= [
  "snail",
  "booba",
  "sad",
  "depressed", "unhappy", "angry", "miserable", "sadge" , "discontent" , ":peeposad:" , ":pepehands:"
]

if "responding" not in db.keys(): 
  db["responding"] = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="netscape"))
    print("Moderation Bot Online and Running")

cult_words = db["cult"]
@client.event
async def on_message(message):
  msg = message.content

  if message.author == client.user:
    return
  if msg.startswith('$hi'):
    await message.channel.send('Hello!')
  if msg.startswith('$snail'):
    await message.channel.send('JOIN THE CULT')
  if any(word in msg for word in cult_words):
    if db["responding"] is True:
      await message.channel.send(('JOIN THE CULT'))
  
  if msg.startswith('$respond'):
    if db["responding"] is True:
      db["responding"] = False
      await message.channel.send('The bot will stop responding')
    elif db["responding"] is False:
      db["responding"] = True
      await message.channel.send('The bot will start responding')

client.run(secret)

