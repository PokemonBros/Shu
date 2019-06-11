#!/usr/bin/env python

#Imports
import discord  
from discord.ext import commands

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def check_dev(ctx):
        return ctx.author.id == 180852994231762945
    @commands.command()
    @commands.check(check_dev)
    async def eric(self, ctx): 
        useEric = 0
        if useEric == 0:
            await ctx.send('yeet')
            while useEric == 0:
                await ctx.send('Happy Birthday' + '<@!306020235377377281>' + "!")
       


def setup(bot):
    bot.add_cog(Developer(bot))
       