import discord
from discord.ext import commands
from discord.utils import get
import sys

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):
        embed1 = discord.Embed(title="COMMANDS", colour=discord.Colour(0x22ff3e))
        embed1.set_footer(text=f"Ping: {round(self.bot.latency * 1000)}ms")
        embed1.add_field(name="help", value="shows this command", inline=False)
        embed1.add_field(name="operator", value="shows the supportet operators", inline=False)
        embed1.add_field(name="versions", value="discord.py and python version", inline=False)
        await ctx.send(embed=embed1)

    @commands.command()
    async def versions(self, ctx):
        embed0 = discord.Embed(colour=discord.Colour(0x02fb09))
        embed0.add_field(name="Python", value=f"[{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}](https://www.python.org/)")
        embed0.add_field(name="\u200B", value="\u200B")
        embed0.add_field(name="Discord.py", value=f"[{discord.__version__}](https://github.com/Rapptz/discord.py)")
        await ctx.send(embed=embed0)

    @commands.command()
    async def operator(self, ctx):
        embed0 = discord.Embed(colour=discord.Colour(0x02fb09))
        embed0.add_field(name="+", value="addition", inline=False)
        embed0.add_field(name="-", value="subtract", inline=False)
        embed0.add_field(name="*", value="multiplication", inline=False)
        embed0.add_field(name="/", value="division", inline=False)
        embed0.add_field(name="%", value="modulas", inline=False)

        await ctx.send(embed=embed0)

def setup(bot):
    bot.add_cog(misc(bot))

