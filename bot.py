import time

import discord
from discord.ext import commands

import config


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {0}!'.format(bot))


@bot.command()
async def ping(ctx):
    """Returns the bots ping in milliseconds."""
    start = time.perf_counter()
    await ctx.channel.trigger_typing()
    end = time.perf_counter()

    duration = (end - start) * 1000
    await ctx.send("Pong! Took `{0:.2f}ms`".format(duration))


bot.run(config.TOKEN)
