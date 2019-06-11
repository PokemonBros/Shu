#!/usr/bin/env python

#Imports
import discord  
import random
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rroulette(self, ctx, userid2: str): 
        userid1 = ctx.author.id
        await ctx.send('You have been invited to play russian roulette ' + userid2 + "." + " Do you accept? Y/N")
        
        await ctx.send('Welcome to russian roulette.')
    @commands.command()
    async def rps(self, ctx, user_input: str): 
        cpu_rps = ["rock", "paper", "scissors"]
        cpu_choice = random.choice(cpu_rps)
        user_choice = user_input.lower()
        if user_choice == "rock":
            if cpu_choice == "rock":
                await ctx.send("You have tied with a bot. Shows you why you\'re being replaced.")
            if cpu_choice == "paper":
                await ctx.send("You won. Congratulations, it's a celebration, hopefully this doesn\'t earn me a demonitization.")
            if cpu_choice == "scissors":
                await ctx.send("Yikes. You feeling like pennies?")
        if user_choice == "paper":
            if cpu_choice == "rock":
                await ctx.send("Yikes. You feeling like pennies?")
            if cpu_choice == "paper":
                await ctx.send("You have tied with a bot. Shows you why you\'re being replaced.")
            if cpu_choice == "scissors":
                await ctx.send("You won. Congratulations, it's a celebration, hopefully this doesn\'t earn me a demonitization.")
        if user_choice == "scissors":
            if cpu_choice == "rock":
                await ctx.send("Yikes. You feeling like pennies?")
            if cpu_choice == "paper":
                await ctx.send("You won. Congratulations, it's a celebration, hopefully this doesn\'t earn me a demonitization.")
            if cpu_choice == "scissors":
                await ctx.send("You have tied with a bot. Shows you why you\'re being replaced.")

        



def setup(bot):
    bot.add_cog(Game(bot))
          