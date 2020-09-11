import praw

##### REDDIT

reddit = praw.Reddit(client_id='YourId',
                    client_secret = 'YourSecret' ,
                    username ='YourUsername' ,
                    password = 'YourPassword',
                    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36')

#Check the praw documentation if you have questions (You get these (exept user agent) when you create an app whithin a Reddit)
# reddit.com/prefs/apps/
#####




#####DISCORD

TOKEN = 'YOUR TOKEN'#You can find it when the bot application created here: discord.com/developers/applications

#####
