import discord
import random
import time
import asyncio

TOKEN = "NzY5MjkxNzc2MjI4ODUxNzIz.X5M4zA.3FiL3gmJblbtNGGJUznA2agpNNI"

client = discord.Client()
images = ["https://imgur.com/a/nVxLm9w", "https://imgur.com/a/LjmiVDJ", "https://imgur.com/a/D7f3ufu"]
pb = ["https://imgur.com/a/nVxLm9w", "https://imgur.com/a/D7f3ufu"]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".test"):
        await message.channel.send("Shut the fuck up")

    if message.content.startswith(".say"):
        mes = message.content.split()
        output = ""
        for word in mes[1:]:
            output += word
            output += " "
        await message.channel.send(output)

    if message.content.startswith(".help"):
        embed = discord.Embed(title="__Commands__", color=0x00ff00)
        embed.add_field(name=".help", value="Shows this message")
        embed.add_field(name=".say", value="Replies with whatever you said")
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith(".blue"):
        await message.channel.send("https://imgur.com/a/nVxLm9w")

    if message.content.startswith(".orange"):
        await message.channel.send("https://imgur.com/a/LjmiVDJ")

    if message.content.startswith(".random"):
        await message.channel.send(random.choice(images))

    if message.content.startswith(".pb"):
        await message.channel.send(random.choice(pb))




@client.event
async def on_ready():
    print("RUNNING")

client.run(TOKEN)
