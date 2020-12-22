import discord, os, requests, json, lockedsecret, random
from keep_alive import keep_alive

client = discord.Client()
token = lockedsecret.TOKEN
game = lockedsecret.GAME
tvshow = lockedsecret.TVSHOW
music = lockedsecret.MUSIC
randomint = random.randrange(1,3)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('Random number is {0}'.format(randomint))
    if randomint == 1:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=tvshow))
    elif randomint == 2:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=music))
    else:
        await client.change_presence(activity=discord.Game(game))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Prevents the bot from responding to itself :)
    if message.author == client.user:
        return  

    # A whole new beginning
    if message.content.startswith('$hello'):
        await message.channel.send('Hello m8! How are you doing today {0}'.format(message.author.mention))

    # Vibe Check
    if message.content.startswith('$vibecheck'):
        await message.channel.send('<:vibin:737290870583197757> YO, WE GOT A VIBE CHECK OVER HERE <:vibin:737290870583197757> ')

    # A whole new beginning
    if message.content.startswith('$siege'):
        await message.channel.send('Gaming tonight {0} ?'.format(message.author.mention))

    # Inspiring messages (random)
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send('Here you go {0}: {1}'.format(message.author.mention, quote))

# Uncomment in production
# keep_alive()

client.run(token)
