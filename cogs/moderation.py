import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    

    

    @commands.command(
        name="unban",
        description="A command which unbans a given user",
        usage="<user> [reason]",
    )
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason=reason)

        channel = self.bot.get_channel(704301090471936253)
        embed = discord.Embed(
            title=f"{ctx.author.name} unbanned: {member.name}", description=reason
        )
        await channel.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Moderation(bot))