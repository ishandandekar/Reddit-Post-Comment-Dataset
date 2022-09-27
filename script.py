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

# Writing .txt files
subreddits = ['confessions', 'tifu', 'talesfromtechsupport',
              'IDontWorkHereLady', 'LetsNotMeet']

# Setting up multiple loops for automation
for subreddit in subreddits:
    for submission in reddit_client.subreddit(subreddit).top(limit=1):
        post_count = 0
        comments_list = submission.comments.list()[:15]
        for comment in comments_list:
            with open(f'data/{subreddit}.txt', 'a') as f:
                f.write(f'# {post_count}\n')
                f.write(f'## r/confessions\n')
                f.write(f'### {submission.title}\n')
                f.write(f'#### {submission.url}\n')
                f.write(
                    f'##### {comment.body.encode("utf-8", errors="ignore")}\n\n')
            post_count += 1
