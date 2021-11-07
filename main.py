import discord
import os
import asyncio
from discord.ext import commands
from map import MapNode
from map import Map
from discord.utils import get
import requests
custom_prefixes = {}
global customtime
customtime = 100
global upcount
upcount = 0
global downcount
downcount = 0
global rightcount
rightcount = 0
global leftcount
leftcount = 0
start = False
secret = os.environ['Token']
Tenor_Token = os.environ['Tenor_Token']
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

def get_gif(searchTerm): 

    response = requests.get("https://g.tenor.com/v1/search?q={}&key={}&limit=1".format(searchTerm, Tenor_Token))

    data = response.json()  

         
    return data['results'][0]['media'][0]['gif']['url']



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
    gif_url = get_gif(Current.Curr.dataval) 
    embed = discord.Embed()
    embed.set_image(url=gif_url)
    await message.channel.send(embed=embed)
    await output.add_reaction("▶️")
    await output.add_reaction("◀️")
    await output.add_reaction("🔽")
    await output.add_reaction("🔼")
    time = customtime
    await asyncio.sleep(10)
    up = upcount
    down = downcount
    right = rightcount
    left = leftcount
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


  if msg.startswith('$adventure') and not (msg.startswith('$adventure time')):  
    client.loop.create_task(adventure(message , generatemap()))
    await message.channel.send('The adventure has begun.')
  
  if msg.startswith('$adventure time'):
    global customtime
    await message.channel.send('Inserted time')
    customtime = (message.content.lower()[16:])
  
client.run(secret)

