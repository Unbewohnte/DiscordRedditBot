from authentication import TOKEN, reddit
import discord
from discord.ext import commands
from functions import *

client  = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
	print('=======================================================')
	print('                       READY                           ')
	print('=======================================================')
	await client.change_presence(activity = discord.Game('game'))
	#You can delete this ↑↑↑ line if you don`t want your bot to have an activity showing


@client.command()
async def parse_hot(ctx, subreddit , how_many = 5):
    await ctx.send('Okay, the subreddit is : r/{}; I`ll show you {} posts in hot'.format(str(subreddit), str(how_many)))
    url_opn_list.clear()
    try:
        reddit_parse_hot(reddit,str(subreddit),int(how_many))
        for url in url_opn_list:
            await ctx.send(url)
    except Exception as error:
        await ctx.send('Error : '+ str(error)+ '\n')

@client.command()
async def parse_time(ctx, subreddit, how_many = 5):
    await ctx.send('Okay, the subreddit is : r/{}; I`ll show you {} posts based on time'.format(str(subreddit), str(how_many)))
    url_opn_list.clear()
    try:
        reddit_parse_time(reddit,str(subreddit),int(how_many))
        for url in url_opn_list:
            await ctx.send(url)
    except Exception as error:
        await ctx.send('Error : '+ str(error)+ '\n')


@client.command()
async def check(ctx):
	await ctx.send(' ```css' +'\n'+ '[Online]' + '\n'+ '```')


@client.command()
async def random(ctx,how_many = 5):
	url_opn_list.clear()
	try:
		what_to_parse = random_subreddit(reddit,int(how_many))[1]
		await ctx.send('Aaaand... The subreddit is: r/{}. I`ll show you {} posts in hot'.format(str(what_to_parse),str(how_many)))
		for url in url_opn_list:
			await ctx.send(url)
	except Exception as error:
 		await ctx.send('Error : '+ str(error)+ '\n')


client.run(TOKEN)
