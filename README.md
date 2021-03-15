# Discord Bot 
Following this tutorial from freeCodeCamp - <a href="https://www.freecodecamp.org/news/create-a-discord-bot-with-python/">Link</a>

This tutorial will show you how to build your own Discord bot completely in the cloud. You do not need to install anything on your computer, and you do not need to pay anything to host your bot. We are going to use a number of tools, including the Discord API, Python libraries, and a cloud computing platform called Repl.it.  There is also a video version of this written tutorial. The video is embedded below and the written version is after the video.


<br>
<hr>
<div align="center">

## Required Tools (How to Install)
</div>
<hr>

<br>

Make an env file with your bot-token and utilities.  Use the EXAMPLE file as a guide. 
```
// .env file

TOKEN = "your-token-goes-here-1A2B3C4D5E6FG7H8"
GAME = "Chess"
TVSHOW = "Friends"
MUSIC = "Kanye West"
NASA = "your-specific-nasa-api-key-here-1A2B3C4D5E6FG7H8"
apodCHAN = "your-APOD-channel-in-your-Discord-123456789"

```

<br>

<br>

Discord API Dependency 
```
pip install discord 
```

US Holidays Dependency 
```
pip install holidays 
```

Schedule Dependency 
```
pip install schedule
```
<br>



<br>
<hr>
<div align="center">

## Bug Fixes
</div>
<hr>
<br>

To use custom emojis within your discord bots responses (<a href="https://www.reddit.com/r/discordapp/comments/54ygeb/sexualrhinoceros_music_bot_cant_use_custom_emojis/">LINK</a>): 
```
Bot's can't use emoji's direcly, they need to use an emoji-ID.

So, in your server type \:vibin: and it will give you something like this: <:vibin:737290870583197757>

Copy that whole thing (with the < and >) and paste that in the response text that the bot should say. Each custom emoji-ID looks like this <:emojiname:numbers> and when you send a emoji then your app will auto convert it to the ID, this does not happens with bots so for bots you need to set it manualy
```

<br>

Bots pretty much ignore bots to prevent endless loops of death (<a href="https://www.reddit.com/r/discordapp/comments/5j0pnv/discord_net_bot_talking_to_another_bot/">LINK</a>):

```
Erisbot is likely ignoring the message by checking if it's sent from a bot. Bot to bot interactions should be avoided because it can cause loops of bots just replying to each other.

just going to have to code your own features :) 
```

<br>

To set custom status messages for your bot - use client.change_presence (<a href="https://medium.com/python-in-plain-english/how-to-change-discord-bot-status-with-discord-py-39219c8fceea">LINK</a>):

```
// Main.py (Line 15)

// Gaming
await client.change_presence(activity=discord.Game('Rainbow 6 Siege'))

// Streaming
await client.change_presence(activity=discord.Streaming(name='Roblox', url='https://www.twitch.tv/your_channel'))

// Watching
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='The Office'))

// Listening 
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Kids See Ghosts'))
```