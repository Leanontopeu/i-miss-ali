import os
import discord

TOKEN = os.environ.get("MTQ3MDQ1NTMwMjMxMzg2OTQ4NQ.Gny9_")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.Playing name="I miss my ali :c"
                                                                                           )
                                                        )
  client.run(TOKEN)
