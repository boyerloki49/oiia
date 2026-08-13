import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

FRAMES = [
    "```ansi\n\u001b[1;31m  🎵 [🔊 MAX VOLUME] 🎵\n    /\\_/\\\n   (  o.o )  ✈️  *flying through red space*\n    > ^ <\n```",
    "```ansi\n\u001b[1;34m  🎵 [🔊 BASS DROP!] 🎵\n      /\\_/\\\n     (  -.- )  ✈️  *flying through blue space*\n      > ^ <\n```",
    "```ansi\n\u001b[1;35m  🎵 [🔊 DRIFT INTENSIFIES] 🎵\n        /\\_/\\\n       (  >=< )  ✈️  *flying through purple space*\n        > ^ <\n```",
    "```ansi\n\u001b[1;32m  🎵 [🔊 PHONK] 🎵\n          /\\_/\\\n         (  o.o )  ✈️  *flying through green space*\n          > ^ <\n```",
    "```ansi\n\u001b[1;36m  🎵 [🚀 HYPERSPACE GALAXY] 🚀\n          /\\_/\\\n         (  O.O )  ✨ *entering galaxy*\n          > ^ <\n```"
]

@bot.command()
async def oiia(ctx):
    msg = await ctx.send(FRAMES[0])
    for _ in range(3):
        for frame in FRAMES:
            await asyncio.sleep(0.6)
            await msg.edit(content=frame)
    await asyncio.sleep(1)
    await msg.delete()

import os
bot.run(os.getenv("MTUzNzMxMTkxMTM0MTg1NDczMA.G-u_Ux.9AuCwPSEfKVrZWODFGu1fr374IgPJuQNSF3saQ"))

