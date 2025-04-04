import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # Only add reactions to messages in a specific channel
    if message.channel.name == '<your-channel-name>':
        # Add reactions to the message. You can customize the emojis as needed.
        await message.add_reaction('🛡️')
        await message.add_reaction('💜')
        await message.add_reaction('🤝')
        await message.add_reaction('🔥')

# Run the bot (replace "YOUR_BOT_TOKEN" with your actual bot token)
client.run("YOUR_BOT_TOKEN")
