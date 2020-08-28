import praw
import json
import bs4

client_id = "wXjj_0hwbO5dTg"
client_secret = "WMvdCOiqXDnBb1rnRsu7v7-IvVM"
user_agent = "scrape_api"
username = "pyprog1"
password = "MKEprog"

reddit = praw.Reddit(client_id = "wXjj_0hwbO5dTg", client_secret = "WMvdCOiqXDnBb1rnRsu7v7-IvVM", user_agent = "scrape_api", password = "MKEprog")

subreddit = reddit.subreddit("buildapcsales")

hot_results = subreddit.hot(limit = 10)
new_results = subreddit.new(limit = 10)
controv_results = subreddit.controversial(limit = 10)
top_results = subreddit.top(limit = 10)


for submission in hot_results:
    if not submission.stickied:
        print('Title: {}, score: {}, id: {}, url: {}, num_comments: {}, created: {}'.format(submission.title, submission.score, submission.id, submission.url, submission.num_comments, submission.created))

# for submission in new_results:
#     if not submission.stickied:
#         print('Title: {}, score: {}, id: {}, url: {}, num_comments: {}, created: {}'.format(submission.title, submission.score, submission.id, submission.url, submission.num_comments, submission.created))

# for submission in controv_results:
#     if not submission.stickied:
#         print('Title: {}, score: {}, id: {}, url: {}, num_comments: {}, created: {}'.format(submission.title, submission.score, submission.id, submission.url, submission.num_comments, submission.created))

# for submission in top_results:
#     if not submission.stickied:
#         print('Title: {}, score: {}, id: {}, url: {}, num_comments: {}, created: {}'.format(submission.title, submission.score, submission.id, submission.url, submission.num_comments, submission.created))

 
# submission tag reference
# 'link_flair_text': 'RAM',