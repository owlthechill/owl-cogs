from .reactions import ReactionCog

async def setup(bot):
    await bot.add_cog(ReactionCog(bot))