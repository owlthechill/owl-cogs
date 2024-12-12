import discord
from redbot.core import commands

class ReactionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        # Send a reaction
        await ctx.message.add_reaction("🐕‍🦺")

