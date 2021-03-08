import discord, os, requests, json, lockedsecret, random, holidays
from datetime import date
from keep_alive import keep_alive

client = discord.Client()
token = lockedsecret.TOKEN
game = lockedsecret.GAME
tvshow = lockedsecret.TVSHOW
music = lockedsecret.MUSIC
randomint = random.randrange(1,3)
us_holidays = holidays.US()
today = date.today()
test = "7-4-2022"

# Get an inspiring quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


def get_roast():
    response = requests.get("https://insult.mattbas.org/api/insult?who={0}".format(""))
    message = response.content.decode("utf-8")
    return message


# Detect Holiday
def is_holiday(u):
    if (today in us_holidays):
        return "Haven't you heard {0}? Today is {1}".format(u, us_holidays.get(today))
    else:
        return "Today is not an official United States holiday, but it's National {0} Day in this server! ".format(u)


# Set behavior activity within discord. 
@client.event
async def on_ready():
    print('Random number is {0}'.format(randomint))
    if randomint == 1:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=tvshow))
    elif randomint == 2:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=music))
    else:
        await client.change_presence(activity=discord.Game(game))
    print("{0} - We are logged in as {1.user}".format(today, client))

@client.event
async def on_message(message):
    # Prevents the bot from responding to itself :)
    if message.author == client.user:
        return  
    
    # Help
    if message.content.startswith('.help'):
        await message.channel.send('Here you go {0}: \n .help \n .hello \n .vibe \n .siege \n .inspire \n .roast \n .holiday \n .yeti'.format(message.author.mention))

    # A whole new beginning
    if message.content.startswith('.hello'):
        await message.channel.send('Hello mate! How are you doing today {0}'.format(message.author.mention))

    # Vibe Check
    if message.content.startswith('.vibe'):
        await message.channel.send('<:vibin:737290870583197757> YO, WE GOT A VIBE CHECK OVER HERE <:vibin:737290870583197757> ')

    # A whole new beginning
    if message.content.startswith('.siege'):
        await message.channel.send('Gaming tonight {0} ?'.format(message.author.mention))

    # Inspiring messages (random)
    if message.content.startswith('.inspire'):
        quote = get_quote()
        await message.channel.send('Here you go {0}: \n \n {1}'.format(message.author.mention, quote))

    # Roast
    if message.content.startswith('.roast'): 
        await message.channel.send("{0}, {1}".format(message.author.mention, get_roast()))

    # Holiday
    if message.content.startswith('.holiday'):
        await message.channel.send(is_holiday(message.author.mention))
    
    # Holiday
    if message.content.startswith('.yeti'):
        await message.channel.send("https://twitch.tv/yeti")

    
# Uncomment in production
# keep_alive()

client.run(token)
