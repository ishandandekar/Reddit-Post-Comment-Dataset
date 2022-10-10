# Importing libraries
import praw
import os
from dotenv import load_dotenv

# Setup
load_dotenv()
reddit_client = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT')
)
DATA_DIR = os.path.join(os.getcwd(), 'data')
print(f"Storing all the data in this directory: {DATA_DIR}")

# Writing .txt files
subreddits = ['confessions', 'tifu', 'talesfromtechsupport', 'IDontWorkHereLady',
              'LetsNotMeet', 'AskReddit', 'todayilearned', 'explainlikeimfive', 'IAmA', 'FanTheories', 'gonewildstories', 'UnethicalLifeProTips']

# Setting up multiple loops for automation
# for subreddit in subreddits:
#     PATH = os.path.join(DATA_DIR, subreddit)
#     os.mkdir(PATH)
#     for submission in reddit_client.subreddit(subreddit).top(limit=15):
#         post_id = 0
#         comments_list = submission.comments.list()[:15]
#         for comment in comments_list:
#             data_id = 0
#             with open(os.path.join(PATH, f'post_{post_id}.txt'), 'a') as f:
#                 f.write(f'# {data_id}\n')
#                 f.write(f'## r/{subreddit}\n')
#                 f.write(f'### {submission.title}\n')
#                 f.write(
#                     f'#### {submission.selftext.encode("utf-8", errors="ignore")}\n')
#                 f.write(f'##### {submission.url}\n')
#                 f.write(
#                     f'###### {comment.body.encode("utf-8", errors="ignore")}\n\n')
#             data_id += 1
#         post_id += 1
#     break

# Setting up multiple loops for automation
for subreddit in subreddits:
    PATH = os.path.join(DATA_DIR, subreddit)
    os.mkdir(PATH)
    post_id = 0
    for submission in reddit_client.subreddit(subreddit).top(limit=15):
        with open(os.path.join(PATH, f'post_{post_id}.txt'), 'a') as f:
            f.write(f'# r/{subreddit}\n')
            f.write(f'## {submission.title}\n')
            f.write(
                f'#### {submission.selftext.encode("utf-8", errors="ignore")}\n\n')
            comments_list = submission.comments.list()[:15]
            for comment in comments_list:
                f.write(
                    f'###### {comment.body.encode("utf-8", errors="ignore")}\n')
        post_id += 1
    break
