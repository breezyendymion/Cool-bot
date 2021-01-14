import discord
import random
import io
import datetime
from datetime import time
from time import sleep
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
client.remove_command('help')
client.remove_command('ban')
client.remove_command('unban')
client.remove_command('kick')

@client.event
async def on_ready():
    status_list = open('phrases.txt', encoding = "utf8").read().splitlines()
    await client.change_presence(status=discord.Status.online, activity = discord.Game(random.choice(status_list)))

@client.event
async def on_message(message):
    if message.author.bot == True:
        return
    number = open('value.txt', encoding = "utf-8").read()
    value = random.randrange(int(number))
    if value == 0:
        phrase_list = open('phrases.txt', encoding = "utf-8").read().splitlines()
        channel_typing = client.get_channel(message.channel.id)
        async with channel_typing.typing():
            sleep(1)    
        phrase = random.choice(phrase_list)
        await message.channel.send(phrase)
    with io.open("phrases.txt", "a", encoding = "utf-8") as output:
        output.write(message.content + '\n')
    await client.process_commands(message)

@client.command()
async def setchance(ctx, value = None):
    if ctx.author.id != 488051426757574667:
        return
    if value == None:
        await ctx.send('Please chose a value to set')
        return
    if value == 0:
        await ctx.send('Value must be more than 0')
        return
    if value.isnumeric() == True:
        with io.open("value.txt", "w", encoding = "utf-8") as output:
            output.write(value)
        await ctx.send('Chance set to ' + value)
    else:
        await ctx.send('Value is not a number')

token = open('token.txt').read()
client.run(token) 