import discord
from discord.ext import commands
from discord.utils import get
import operator
import sys

class calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ops = {'+' : operator.add,'-' : operator.sub,'*' : operator.mul,'/' : operator.truediv,'%' : operator.mod,'^' : operator.xor}

    @commands.Cog.listener()
    async def on_message(self, message):
        query = message.content.split()
        extracted = []
        for i in query:
            try:
                if i in self.ops.keys():
                    extracted.append(i)
                else:
                    extracted.append(float(i))
            except:
                pass
        try:
            if len(extracted)/3 == 1:
                await message.channel.send(f"{message.author.mention} {extracted[0]} {extracted[1]} {extracted[2]} = {self.ops[extracted[1]](extracted[0], extracted[2])}")
        except:
            return
            
                

        


def setup(bot):
    bot.add_cog(calc(bot))

