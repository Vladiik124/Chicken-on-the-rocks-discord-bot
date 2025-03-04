import discord
import datetime
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def send_chicken_rocks():
    await client.wait_until_ready()

    # Use channel from .env or fallback to hardcoded ID
    channel_id = int(os.getenv("CHANNEL_ID"))
    channel = client.get_channel(channel_id)

    if not channel:
        print("❌ Channel not found. Check the CHANNEL_ID value.")
        return

    print(f"✅ Sending messages to: #{channel.name} (ID: {channel_id})")

    flag = True
    while not client.is_closed():
        now = datetime.datetime.now()
        if (now.hour == 0 or now.hour == 12) and now.minute == 0:
            if flag:
                print("🎥 Sending video...")
                await channel.send("https://cdn.discordapp.com/attachments/1338253868840259644/1339024455157940234/Jbh3pVR5gqUYS2rV.mp4")
                flag = False

        if now.hour not in [0, 12] or now.minute > 1:
            flag = True

        await asyncio.sleep(60)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    client.loop.create_task(send_chicken_rocks())

client.run(os.getenv('TOKEN'))
