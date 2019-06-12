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
        if user_choice == cpu_choice:
            await ctx.send("You have tied with a bot. Shows you why you\'re being replaced.")
        else:
            if user_choice == "rock":
                if cpu_choice == "paper":
                    await ctx.send("You won. Congratulations, it's a celebration, hopefully this doesn\'t earn me a demonitization.")
                if cpu_choice == "scissors":
                    await ctx.send("Yikes. You lost. You feeling like pennies?")
            if user_choice == "paper":
                if cpu_choice == "rock":
                    await ctx.send("Yikes. You lost. You feeling like pennies?")
                if cpu_choice == "scissors":
                    await ctx.send("You won. Congratulations, it's a celebration, hopefully this doesn\'t earn me a demonitization.")
            if user_choice == "scissors":
                if cpu_choice == "rock":
                    await ctx.send("Yikes. You lost. You feeling like pennies?")
                if cpu_choice == "paper":
                    await ctx.send("You won. Congratulations, it's a celebration, hopefully this doesn\'t earn me a demonitization.")
    @commands.command()
    async def magic8(self, ctx,): 
        userid1 = ctx.author.id
        shake_numbers = ["1", "2", "3"]
        shake = random.choice(shake_numbers)
        await ctx.send('You shook the magic 8 ball ' + shake + " times.")
        if userid1 == 120195047470661632:
            await ctx.send('There is no hope left for you...')
        elif userid1 == 393160457508225036:
            await ctx.send('Anata wa pesuto kara yūtopia o kōchiku shi, tetsu no ken de sekai o shihai surudeshou. Senpai otōsan.')
        elif userid1 == 357953549738573835:
            await ctx.send('Egg.')
        elif userid1 == 180852994231762945:
            await ctx.send('Your only future is being pushed later by you... Stop procrastinating.')
        else:
            if shake == "1":
                await ctx.send('http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html')
            if shake == "2":
                await ctx.send('I think you would love a homeowners insurance.')
            if shake == "3":
                await ctx.send('My man Mahmud. What you think you doin eh? Go get workin on those sunflowers my dude.')
          



def setup(bot):
    bot.add_cog(Game(bot))
          