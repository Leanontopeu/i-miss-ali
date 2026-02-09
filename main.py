import os
import discord

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="i miss ali :c"
        )
    )

client.run(TOKEN)
