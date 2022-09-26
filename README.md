# Reddit_Post_Comment_Dataset

## Contribution

Although this is not a conventional open-source project, if you find any errors (even a typo!) and/or want to improve something in the repository, and/or want to help document the project, feel free to create a pull request! 😄

#### Resources to use:

1. Praw
1. BeautifulSoup
1. Selenium
1. [Python Engineer's tutorial](https://www.youtube.com/watch?v=8VZhog5C3bU&ab_channel=PythonEngineer)
1. [Python script](https://github.com/gabrielpreda/reddit_extract_content/blob/main/reddit_ask_reddit.py)

#### TODO:

- [ ] Fix link to scrape only top posts
- [ ] Figure out how to scrape comments
- [ ] Find subreddits with populated text posts
- [ ] Make `txt` dataset in following format:

  ```
  # <id>
  ## r/<name of the subreddit X>
  ### <upvotes>
  ### <post title>
  #### <single comment from the post>

  # <id>
  ## r/<name of the subreddit X>
  ### <upvotes>
  ### <post title>
  #### <single comment from the post>

  # <id>
  ## r/<name of the subreddit Y>
  ### <upvotes>
  ### <post title>
  #### <single comment from the post>
  ```

- [ ] Publish dataset to kaggle
