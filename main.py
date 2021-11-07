import discord
import os
import asyncio
from discord.ext import commands
from map import MapNode
from map import Map
from discord.utils import get

start = False
secret = os.environ['Token']
def generatemap():
  Home = MapNode("This is Home")
  Lefttown = MapNode("This is LeftTown")
  Uptown = MapNode("This is UpTown")
  Home.insert(Lefttown ,3) 
  Home.insert(Uptown, 1)
  Downtown = MapNode("This is DownTown")
  Home.insert(Downtown, 4)
  Righttown = MapNode("This is RightTown")
  Home.insert(Righttown, 2)
  Current = Map(Home)
  return Current

client = commands.Bot(command_prefix = "$")
@client.event
async def on_raw_reaction_add(payload):
  channel = client.get_channel(906579155238395916)
  (payload.message_id)
  message = await channel.fetch_message(payload.message_id)
  if payload.emoji.name == "◀️":
    reaction = get(message.reactions, emoji="◀️")
    global leftcount
    leftcount = reaction.count
  if payload.emoji.name == "▶️":
    reaction = get(message.reactions, emoji="▶️")
    global rightcount
    rightcount = reaction.count
  if payload.emoji.name == "🔽":
    reaction = get(message.reactions, emoji="🔽")
    global downcount
    downcount = reaction.count
  if payload.emoji.name == "🔼":
    reaction = get(message.reactions, emoji="🔼")
    global upcount 
    upcount = reaction.count

@client.event
async def adventure(message , Current):
  await message.channel.send("Welcome to your grand new adventure, work together with your friends to explore the world")
  while True:
    output = await message.channel.send(Current.Curr.dataval)
    await output.add_reaction("▶️")
    await output.add_reaction("◀️")
    await output.add_reaction("🔽")
    await output.add_reaction("🔼")
    await asyncio.sleep(10)
    up = upcount
    down = downcount
    right = rightcount
    left = leftcount
    await message.channel.send(up)
    await message.channel.send(down)
    await message.channel.send(right)
    await message.channel.send(left)
    check = False
    numbers = [right,left,up,down]
    numbers.sort(reverse=True)
    if (numbers[0] == numbers[1]):
      check = False
    elif(max(numbers) == up):
      if Current.Curr.up is None:
        check = False
      else:
        check =Current.goNext(1)
        await message.channel.send('you went North')
    elif(max(numbers) == right):
      if Current.Curr.right is None:
        check = False
      else:
        check =Current.goNext(2)
        await message.channel.send('you went East')
    elif(max(numbers) == left):
      if Current.Curr.left is None:
        check = False
      else:
        check =Current.goNext(3)
        await message.channel.send('you went West')
    elif(max(numbers) == down):
      if Current.Curr.down is None:
        check = False
      else:
        check =Current.goNext(4)
        await message.channel.send('you went south')

    if check is False:
      await message.channel.send('cannot go that way')

    



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


  if msg.startswith('$adventure'):  
    client.loop.create_task(adventure(message , generatemap()))
    await message.channel.send('The adventure has begun.')
  
      
  
client.run(secret)

