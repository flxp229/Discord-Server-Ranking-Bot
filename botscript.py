import discord
from discord.ext import commands
import requests
import json
import datetime

bot = commands.Bot(command_prefix='!')

# API key for Rocket League API
api_key = "YOUR_API_KEY_HERE"

# Dictionary to match ranks to roles
ranks = {
    "Bronze I": "Rocket League - Bronze",
    "Bronze II": "Rocket League - Bronze",
    "Bronze III": "Rocket League - Bronze",
    "Silver I": "Rocket League - Silver",
    "Silver II": "Rocket League - Silver",
    "Silver III": "Rocket League - Silver",
    "Gold I": "Rocket League - Gold",
    "Gold II": "Rocket League - Gold",
    "Gold III": "Rocket League - Gold",
    "Platinum I": "Rocket League - Platinum",
    "Platinum II": "Rocket League - Platinum",
    "Platinum III": "Rocket League - Platinum",
    "Diamond I": "Rocket League - Diamond",
    "Diamond II": "Rocket League - Diamond",
    "Diamond III": "Rocket League - Diamond",
    "Champion I": "Rocket League - Champion",
    "Champion II": "Rocket League - Champion",
    "Champion III": "Rocket League - Champion",
    "Grand Champion I": "Rocket League - Grand Champion",
    "Grand Champion II": "Rocket League - Grand Champion",
    "Grand Champion III": "Rocket League - Grand Champion",
    "Supersonic Legend": "Rocket League - Supersonic Legend"
}

@bot.command(name='getRank', help='Get your Rocket League 2v2 rank')
async def get_rank(ctx, platform, player_name):
    # Check if command is being used in the correct channel
    if ctx.channel.name != "verification":
        return
    # Make API request to get player's rank
    url = f'https://api.rocketleaguestats.com/v1/player?platform_id={platform}&unique_id={player_name}&apikey={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)
    rank = data['data']['attributes']['stats']['rank_2v2']
    # Assign role based on rank
    role = discord.utils.get(ctx.guild.roles, name=ranks[rank])
    await ctx.author.add_roles(role)
    # Send private message with next possible ranking date
    next_rank_date = datetime.datetime.now() + datetime.timedelta(days=7)
    await ctx.author.send(f'You got ranked successfully! Next possible ranking: {next_rank_date}')

bot.run('YOUR_BOT_TOKEN_HERE')
