# This imports the relevant library to use discord

import discord

# This creates the bot
client = discord.Client()

# This is what the bot does once it is ready
@client.event
async def on_ready():
    # This just prints to the terminal to ensure we know it's running
    print('Logged in as')
    print(client.user.name)
    print('---------')

@client.event
async def on_message(msg):
    # If the message is not in a server
    if (msg.guild == None):
        # Get the correct channel to send to
        chan = client.get_channel(341430302662590466)
        # Send an exact copy of the message
        await chan.send(msg.content)

# This contains the relevant bot token, which is deleted for security
# reasons. If you wish to verify the correct bot is running, please
# contact Skye via the bot and she will send you proof of the running
# code
client.run("token")
