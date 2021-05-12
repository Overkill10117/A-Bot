import random

import discord
from discord.ext import commands

import utils.json_loader


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    

def setup(bot):
    bot.add_cog(Config(bot))