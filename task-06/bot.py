import discord
import datetime
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import re
import csv



intents = discord.Intents.default()
intents.typing = False  
intents.presences = False

url = "https://www.espncricinfo.com/live-cricket-score"

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')



@bot.command()
async def ping(ctx):
    await ctx.send("hi")
@bot.command()
async def livescore(ctx): 
    raw_html = requests.get(url).text
    html = BeautifulSoup(raw_html, "lxml")
    live_score_data = html.find("div", attrs={"class": "ds-flex ds-flex-col ds-mt-2 ds-mb-2"}).text

    remarks = html.find("div", attrs = {"ds-text-tight-s ds-font-regular ds-truncate ds-text-typo"})
    print(remarks)

    formatted_str = re.sub(r'(\D)(\d)', r'\1 \2', live_score_data)
    formatted_str = re.sub(r'(\d)(\D)', r'\1 \2', formatted_str)
    formatted_str = re.sub(r'(/)', r' / ', formatted_str)

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    with open("records.csv", mode = 'a', newline ='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([formatted_str])
        csv_writer.writerow([formatted_datetime])
        csv_writer.writerow(["--------------------------------------"]) 
    await ctx.send("Loading live scores...")
    await ctx.send(formatted_str)
    await ctx.send(formatted_datetime)

@bot.command()
async def generate(ctx):
    with open("records.csv", 'rb') as file:
        await ctx.send(file=discord.File(file, "records.csv"))

@bot.command()
async def helpme(ctx):
    await ctx.send("Commands: \n'!generate @Crickey' - get the csv file the livescores are stored in \n'!livescore @Crickey'- get the live scores")
bot.run('MTE1NTc3ODg2MjAyMjY3MjQyNQ.GJmrhS.tgzd_CmEYount_nMTXsMCvYnupX-Pa6DVhB1jY')