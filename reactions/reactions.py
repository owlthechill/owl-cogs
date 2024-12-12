import discord
from redbot.core import commands
import asyncio

reaction_lock = asyncio.Lock()

class ReactionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        # Send a reaction
        async with reaction_lock:
            await asyncio.sleep(1)
            await ctx.message.add_reaction("🐕‍🦺")
            await asyncio.sleep(0.25)
            

