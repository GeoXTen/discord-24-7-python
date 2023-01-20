import discord
import os
import keep_alive

from discord.ext import commands

client = commands.Bot(command_prefix='..', self_bot=True, help_command=None)

# <!-- Import Your Self Bot Commands <3 --> 

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="WhatEverYouGo") # Activity Types :- listening, watching, streaming
    await client.change_presence(status=discord.Status.idle, activity=activity)

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
