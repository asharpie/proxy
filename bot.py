import discord
from discord.ext import commands
import requests
import sys
import time
import datetime

# Variables
bot = commands.Bot(command_prefix='!')


# Commands / Events
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)


@bot.command()
async def proxyhelp(ctx):
    #await ctx.send("`This bot aims to help show which proxies work and which dont.\nHow to use: \nDM me this: !proxytest proxy website\nWhen calling websites do not use 'www' or 'http://'\nExample: \n!proxytest x.x.x.x:xxx(proxy) google.com(website)\nThe Bot will respond with: \n✅ x.x.x.x:xxx - Working on - google.com - Speed: x.x\nLower speed is better! Our speed is based on a calculation of time and requests sent/received so more is worse lower is better! Its posted in m/s`")
    embed = discord.Embed(title="Proxy-Bot Help", color=0x8bc95c)
    embed.add_field(name="!proxytest proxy website", value="You can have as many proxies and website as you want\n", inline=False)
    embed.add_field(name="Warning:", value="Do not attach 'http://' to the website url!!!\n", inline=False)
    embed.add_field(name="Example:", value="!proxytest 1.1.1.1 2.2.2.2 backdoorsneakers.com\n", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def proxytest(ctx, *argv):

    await ctx.send("Working...")

    siteList = [

    ]

    proxies = [

    ]
    baddatalist = [

    ]
    gooddatalist = [

    ]
    speedlist = [

    ]
    for arg in argv:
        if arg.find(".com") == -1:
            argcount = arg.count(":")
            if argcount<=2:
                arg = ":".join(arg.split(":", 2)[:-1])
            else:
                arg = arg
            proxies.append(arg)
            print(proxies)
        else:
            siteList.append(f"http://{arg}")
            print(siteList)

    userAgent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    for site in siteList:
        for proxy in proxies:
            print(proxy)
            speedoriginal = float(0)
            start = time.time()
            try:
                r = requests.get(site, proxies={"http":proxy, "https":proxy}, timeout=5, headers=userAgent)
                end = time.time()
                sped = float("{0:0.2f}".format((end - start) * 1000))
                speed = str(sped)
                print(sped)
                print(site + " - Status Code: " + str(r.status_code))
                await ctx.send("`" + "✅" + proxy + " - Working on - " + site + " - " + "Speed: " + speed + " ms" + "`")
            except:
                end = time.time()
                sped = float("{0:0.2f}".format((end - start) * 1000))
                speed = str(sped)
                print(speed)
                print(site + " - " + "Banned!")
                await ctx.send("`" + "🔴" + proxy + " - Blocked on - " + site + " - " + "Speed: " + speed + " ms" + "`")
    end = 0


@bot.command()
async def testingargs(ctx, *argv):
    await ctx.send("Testing arguments")
    for arg in argv:
        print("Argument:" + arg)


# This will run the bot with the token taken from config.py
bot.run("NDQ1MjU4NzAyNTczMDEwOTc1.DkBorA.5fFIltupPjlhQtVl5nmsdycgZZs")
