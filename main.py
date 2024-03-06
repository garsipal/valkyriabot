import os
os.system("python -m pip install -r requirements.txt")

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!",  activity = discord.Game(name="Valhalla"), intents = discord.Intents().all())

bot.author_id = 487258918465306634  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("Valkyria is ready")

# The channel ID where the bot will, providing it has the necessary permissions, send embedded messages. 
channel_id = 948332733267054623

import random

# Send an embed with particular colors, random messages, and the user's avatar as a thumbnail when a user joins the server.
@bot.event
async def on_member_join(member):
    print('Someone joined the server')
    embed = discord.Embed()
    embed.set_thumbnail(url=member.display_avatar)
    embed.title = ":green_circle: Join"
    welcome_message_list = ['has joined the party', 'has been chosen', 'is here',
                            'has joined us', 'has entered Valhalla', 'has joined the server']          
    welcome_message = welcome_message_list[random.randint(0, len(welcome_message_list) - 1)]
    welcome_comment_list = [':wave:', 'Greetings and salutations.', 'Welcome to the club.',
                            'Welcome!', 'We hope you brought a cake.', "I've been waiting for ages for someone to come along.",
                            "'Ello, 'ello, 'ello!", "Howdy-do!", "How's tricks?", "'Sup, buttercup?",
                            "What's the word, hummingbird?", "What's cookin', good lookin'?",
                            'Ciao!', 'Hola!', 'Hello!',
                            'Hallo!', 'Salut!', 'Hey there.',
                            'Howdy, partner.', "It's good to see you.", 'How is life sailing?',
                            'Enjoy your stay.', 'So, we meet at last.', "Cool.",
                            '']
    welcome_comment = welcome_comment_list[random.randint(0, len(welcome_comment_list) - 1)]
    embed.description = "{} ({}) **{}**.\n".format(member, member.mention, welcome_message) + welcome_comment
    embed.color = 0x78b159
    channel = bot.get_channel(channel_id)
    await channel.send(embed = embed)

# Do the same as above when a user leaves the server. 
@bot.event
async def on_member_remove(member):
    print('Someone left the server')
    embed = discord.Embed()
    embed.set_thumbnail(url=member.display_avatar)
    embed.title = ":red_circle: Leave"
    unwelcome_comment_list = [':wave:', 'Take care, butterfly.', "Don't forget to come back!", "Cheerio!", 
                              "Don't say goodbye!", 'Fare thee well.', "In case I don't see you - good afternoon, good evening, and good night!",
                              "Ta-ta for now!", "Toodle-oo!", "Pip pip!", "Smell you later.", 
                              "Catch you on the flip side!", "Smile, keep calm and wave goodbye....",
                              "Happy trails and all that jazz.",
                              'Bye.', 'What a pity.', 'Catch you on the rebound.',
                              'Adieu!', 'Auf Wiedersehen!', 'Adios.',
                              'Ciao ciao.', 'Au revoir!', "Goodbye and don't cry, we won't.",
                              'It has been emotional.', 'Oh well.', 'It was fun while it lasted.', 
                              'Did I say something wrong?', 'That means more cake for us.', "We will probably never forget you... probably.",
                              '']
    unwelcome_comment = unwelcome_comment_list[random.randint(0, len(unwelcome_comment_list) - 1)]
    embed.description = "{} ({}) **has left the server**.\n".format(member, member.mention) + unwelcome_comment
    embed.color = 0xff473e
    channel = bot.get_channel(channel_id)
    await channel.send(embed = embed)
    
from dotenv import load_dotenv

# Load the .env file containing the token required to run the bot.
load_dotenv()

# Get the token from the .env file.
TOKEN = os.getenv('DISCORD_TOKEN_SECRET')

# Run the bot's token.
bot.run(TOKEN)
