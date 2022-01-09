import os
import discord
import requests
import random
from discord.ext import commands
from replit import db

from keep_alive import keep_alive
intents = discord.Intents().all()
client = discord.Client()
ffxivmsg = "Did you know that the critically acclaimed MMORPG Final Fantasy XIV has a free trial, and includes the entirety of A Realm Reborn AND the award-winning Heavensward expansion up to level 60 with no restrictions on playtime? Sign up, and enjoy Eorzea today! https://secure.square-enix.com/account/app/svc/ffxivregister?lng=en-gb"

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="with your feelings"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    author = str(message.author).split('#', 1)[0]

    if msg.startswith("$hello"):
        print("Message received from", message.author)
        await message.channel.send("Hello")

    if msg.startswith("I am"):
        content = msg.split("I am ", 1)[1]
        dad_message = "Hello, " + content + " I'm Dad!"
        await message.channel.send(dad_message)

    if msg.startswith("$roll"):
        try:
            max = int(msg.split("$roll", 1)[1])
            roll = random.randint(1, max)
        except ValueError:
            roll = random.randint(1, 6)
        roll = str(roll)
        if roll == "69":
            roll = roll + "\nNice"
        await message.channel.send(author + " rolled a " + roll)

    if msg.startswith("$loveme"):
        await message.channel.send("I love you, " + author)

    if msg.startswith("$ffxiv"):
        await message.channel.send(ffxivmsg)

    if msg.startswith("$ff15"):
      channel = client.get_channel(483822111744589866)
      print(type(channel))
      ffmsg = "Its lost, you inted, ff already..."
      for member in channel.members:
        await client.send_message(member, ffmsg)
        await message.channel.send(str(member))
      await message.channel.send(channel.members)


keep_alive()

client.run(os.getenv('TOKEN'))
