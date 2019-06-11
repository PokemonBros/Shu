#!/usr/bin/env python

#Imports
import discord  
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rroulette(self, ctx, userid2: str): 
        userid1 = ctx.author.id
        await ctx.send('You have been invited to play russian roulette ' + userid2 + "." + " Do you accept? Y/N")
        
        await ctx.send('Welcome to russian roulette.')


def setup(bot):
    bot.add_cog(Game(bot))
          