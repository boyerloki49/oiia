import os
import discord
from discord.ext import commands

# This enables all intents automatically so voice tracking works right away
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

OIIA_AUDIO_URL = "https://files.catbox.moe/3p0m7u.mp4"

@bot.event
async def on_voice_state_update(member, before, after):
    # Ignore bot accounts joining channels
    if member.bot:
        return

    # Check if a user joined a voice channel
    if before.channel is None and after.channel is not None:
        voice_channel = after.channel

        # Connect to the voice channel if the bot is not already in one
        if member.guild.voice_client is None:
            vc = await voice_channel.connect()
        else:
            vc = member.guild.voice_client

        # Stop any audio currently playing
        if vc.is_playing():
            vc.stop()

        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

        # Play the audio when you join
        vc.play(discord.FFmpegPCMAudio(OIIA_AUDIO_URL, **ffmpeg_options))

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

bot.run(os.getenv("MTUzNzMyOTc2MDI2MTM4MjI3NA.GjMnPu.lOgw79qkYoBMughZmMd9Ts0PtjLiOuFvwGebvI"))
