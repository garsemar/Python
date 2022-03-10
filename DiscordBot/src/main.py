from discord.ext import commands
import discord
from urllib import parse, request
import datetime
import re
import youtube_dl

bot = commands.Bot(command_prefix='>', description='GarseBot')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)


@bot.command()
async def stats(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description="Info...",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    await ctx.send(embed=embed)


@bot.command()
async def search(ctx, *, src):
    query = parse.urlencode({'search_query': src})
    htmlC = request.urlopen('http://www.youtube.com/results?' + query)
    searchRes = re.findall(r'/watch\?v=(.{11})', htmlC.read().decode())
    await ctx.send(f'https://www.youtube.com/watch?v={searchRes[0]}')


# Play Song
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def play(ctx, url: str):
    pass


# Events
@bot.event
async def on_ready():
    print('Bot ready')


bot.run('ODU4MTUwNDE1NzE1NDAxNzg4.YNZ82g.mXeUr-1CXCJKdTB1kRH9KEgrwWc')
