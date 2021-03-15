import discord, os, requests, json, random, holidays, schedule
from datetime import date
from datetime import datetime
from keep_alive import keep_alive
import time

client = discord.Client()
token = os.getenv("TOKEN")
game = os.getenv("GAME")
tvshow = os.getenv("TVSHOW")
music = os.getenv("MUSIC")
nasaKEY = os.getenv("NASA")
apodCHANNEL = os.getenv("apodCHAN")
randomint = random.randrange(1, 4)
us_holidays = holidays.US()
today = date.today()
now = datetime.now()
current_hour = int(now.strftime("%H"))-5
current_min = int(now.strftime("%M"))
current_sec = int(now.strftime("%S"))


# Get a random number
def get_random():
    randomInt = random.randrange(1, 4)
    return randomInt


# Apod
def get_APOD():
    year = date.today().year
    month = date.today().month
    day = date.today().day
    url = "https://api.nasa.gov/planetary/apod?date={0}-{1}-{2}&api_key={3}".format(year,month,day,nasaKEY)
    response = requests.get(url)
    json_data = json.loads(response.text)
    title = json_data['title']
    image = json_data['url']
    description = json_data['explanation']
    media = json_data['media_type']
    if(media != "image"):
      return "Unfortunately, today's APOD is a video. See you tomorrow!"
    else:
      return title, image, description


# Get an inspiring quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


# Get a spicy roast
def get_roast():
    response = requests.get(
        "https://evilinsult.com/generate_insult.php?lang=en&type=json")
    json_data = json.loads(response.text)
    roast = json_data['insult']
    return (roast)


# Search Function
def searchThis(msg):
  message = msg
  url = 'https://google.com/search?q={0}'.format(message)
  # response = requests.get(url)
  return url
  

# Detect Holiday
def is_holiday(u):
    if (today in us_holidays):
        return "Haven't you heard {0}? Today is {1}".format(
            u, us_holidays.get(today))
    else:
        return "Today is not an official United States holiday, but it's National {0} Day in this server! ".format(
            u)


# APOD Scheduling
def print_apod():
  channel = client.get_channel(819999163130707968)
  myTup = get_APOD()
  (title, url, desc) = myTup
  channel.send(title)
  channel.send(url)
  channel.send(desc)


# Test
def print_me():
  channel = client.get_channel(819999163130707968)
  channel.send("Hello m8")

# Set behavior activity within discord.
@client.event
async def on_ready():
    r = get_random()
    print("{0} - We are logged in as {1.user}".format(today, client))
    print('Random number for activity is {0}'.format(r))
    if r == 1:
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name=tvshow))
    elif r == 2:
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name=music))
    else:
        await client.change_presence(activity=discord.Game(game))


@client.event
async def on_message(message):
    # Prevents the bot from responding to itself :)
    if message.author == client.user:
        return

    # Help
    if message.content.startswith('.help'):
        await message.channel.send(
            'Here you go {0}: \n .help \n .apod \n .hello \n .holiday \n .inspire \n .roast \n .search (coming soon) \n .siege \n .vibe'
            .format(message.author.mention))

    # A whole new beginning
    if message.content.startswith('.hello'):
        await message.channel.send(
            'Hello mate! How are you doing today {0}'.format(
                message.author.mention))

    # Vibe Check
    if message.content.startswith('.vibe'):
        await message.channel.send(
            '<:vibin:737290870583197757> YO, WE GOT A VIBE CHECK OVER HERE <:vibin:737290870583197757> '
        )

    # A whole new beginning
    if message.content.startswith('.siege'):
        await message.channel.send('Gaming tonight {0} ?'.format(
            message.author.mention))

    # Inspiring messages (random)
    if message.content.startswith('.inspire'):
        quote = get_quote()
        await message.channel.send('Here you go {0}: \n \n {1}'.format(
            message.author.mention, quote))

    # Roast
    if message.content.startswith('.roast'):
        r = get_random()
        print('Random number for roast is {0}'.format(r))
        if (r == 1):
            await message.channel.send("Alright, bet.  \n \n {0}, {1}".format(
                message.author.mention, get_roast()))
        elif (r == 2):
            await message.channel.send(
                "Feeling confident today, are we?  \n \n {0}, {1}".format(
                    message.author.mention, get_roast()))
        else:
            await message.channel.send(
                "You asked for it.  \n \n {0}, {1}".format(
                    message.author.mention, get_roast()))

    # Holiday
    if message.content.startswith('.holiday'):
        await message.channel.send(is_holiday(message.author.mention))

    # APOD
    if message.content.startswith('.apod'):
        await message.channel.send(get_APOD()[0])
        await message.channel.send(get_APOD()[1])
        await message.channel.send(get_APOD()[2])

    # Search
    if message.content.startswith('.search'):
        msg = message.content[8:len(message.content)]
        msg = msg.replace(" ", "+")
        await message.channel.send(searchThis(msg))
    
    # test
    if message.content.startswith('.test'):
        await message.channel.send("{0} {1} {2}".format(current_hour, current_min, current_sec))


# Starts the flask web server (comment out in development)
keep_alive()

# Start da bot
client.run(token)