import praw
import urllib
from urllib import request,parse

url_opn_list = []

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'

def reddit_parse_hot(reddit, sub , many):
    what_to_parse = reddit.subreddit(sub)
    hot_posts = what_to_parse.hot(limit = many)
    for post in hot_posts:
        post_url = post.url
        print(post_url)
        req = request.Request(post_url, headers = headers)
        url_opn = request.urlopen(req)
        url_opn_list.append(post_url)
    return url_opn_list

def reddit_parse_time(reddit, sub, many):
    what_to_parse = reddit.subreddit(sub)
    time_posts = what_to_parse.new(limit = many)
    for post in time_posts:
        post_url = post.url
        print(post_url)
        req = request.Request(post_url, headers = headers)
        url_opn = request.urlopen(req)
        url_opn_list.append(post_url)
    return url_opn_list


def random_subreddit(reddit,many):
	what_to_parse = reddit.subreddit('random')
	hot_posts = what_to_parse.hot(limit = many)
	for post in hot_posts:
	    post_url = post.url
	    print(post_url)
	    req = request.Request(post_url, headers = headers)
	    url_opn = request.urlopen(req)
	    url_opn_list.append(post_url)
	return url_opn_list, what_to_parse
