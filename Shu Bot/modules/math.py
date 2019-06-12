#!/usr/bin/env python

#Imports
import discord  
from discord.ext import commands

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rroulette(self, ctx, *, equation : str): 
        equation_numbers = []
        equation_signs = []
        check = True
        temp = ""
        counter = 0
        equation.replace(" ", "")
        while check:
            for letter in equation:
                if letter.isdigit():
                    temp = "" + letter
                    counter++
                
                elif letter == "^":
                    temp = "" + letter
                else
                    temp =
                    break
            equation_numbers.append(temp)
            temp = ""




def setup(bot):
    bot.add_cog(Math(bot))
          