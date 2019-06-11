#!/usr/bin/env python

#Imports
import discord  
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rroulette(self, ctx, *, equation : str): 
        check = True
        temp = ""
        equation.replace(" ", "")
        while check:
            for letter in equation:
                if letter.isdigit():
                    temp = "" + letter
                else
                    break
                

def setup(bot):
    bot.add_cog(Game(bot))
          