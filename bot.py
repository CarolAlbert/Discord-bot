import discord
from discord.ext import commands
import random
from topic import q
from topic import g
from topic import f
c = ('topic/TopicTOPIC : Big questions, TOPIC2/Topic2/topic2 : normal questions, okay/Okay/OKAY: something, com: List of commands, lol/Lol/LOL: random')
dice = ['one', 'two', 'three', 'four', 'five', 'six']
L = 'I CAN SEE YOUR UVULA'

client = commands.Bot(command_prefix="")


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def okay(ctx):
    r = random.choice(f)
    await ctx.send(r)


@client.command()
async def Okay(ctx):
    r = random.choice(f)
    await ctx.send(r)


@client.command()
async def OKAY(ctx):
    r = random.choice(f)
    await ctx.send(r)


@client.command()
async def com(ctx):
    await ctx.send(c)


@client.command()
async def topic(ctx):
    s = random.choice(q)
    await ctx.send(s)


@client.command()
async def Topic(ctx):
    s = random.choice(q)
    await ctx.send(s)


@client.command()
async def TOPIC(ctx):
    s = random.choice(q)
    await ctx.send(s)


@client.command()
async def diceroll(ctx):
    roll = random.choice(dice)
    await ctx.choice(roll)


@client.command()
async def Topic2(ctx):
    v = random.choice(g)
    await ctx.send(v)


@client.command()
async def topic2(ctx):
    v = random.choice(g)
    await ctx.send(v)


@client.command()
async def TOPIC2(ctx):
    v = random.choice(g)
    await ctx.send(v)


@client.command()
async def lol(ctx):
    await ctx.send(L)


@client.command()
async def hello(ctx):
    await ctx.send(Hello)


@client.command()
async def Hello(ctx):
    await ctx.send(Hello)


@client.command()
async def Hi(ctx):
    await ctx.send(Hello)


@client.command()
async def hi(ctx):
    await ctx.send(Hello)


client.run('NzM4NDE5NTMzMDk3OTkyMjI0.XyLoxw.KixkOtChkXTwgOHJ5CctvPquZ08')
