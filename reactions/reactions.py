import discord
from redbot.core import commands

class ReactionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        # This will trigger for any command attempted
        await ctx.send(f"Command {ctx.command} was attempted by {ctx.author}.")
