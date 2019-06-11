#!/usr/bin/env python

#Imports
import discord  
from discord.ext import commands
import typing

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def father(self, ctx): 
        await ctx.send('.')
        await ctx.send('YESN\'T MEN\'T')
        await ctx.send('idk')
        await ctx.send('jk')
        await ctx.send('i don\'t know')
        await ctx.send('YEET')
        await ctx.send('peace out')
        await ctx.send('cool beans')
        await ctx.send('lol k')
        await ctx.send('.')
    @commands.command()
    async def favorite(self, ctx, person: str = "Shu"):
      await ctx.send('My favorite person is {}.'.format(person))
      await client.delete_message(message)
         
   
def setup(bot):
    bot.add_cog(Misc(bot))
                