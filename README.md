# Reddit_Post_Comment_Dataset

**About the dataset :**  
The dataset comprises of top posts from subreddits and comments (related to that post) as a `.txt` file. The posts have been taken from various subreddits, such as, tifu, confessions, IDontWorkHereLady, etc.

**Format of the `.txt` files**

```
# <id>
## <name of the subreddit>
### <title of the post>
#### <post's text or content>
##### <post's url>
###### <comment of the respective post>
.
.
.
# <id>
## <name of the subreddit>
### <title of the post>
#### <post's text or content>
##### <post's url>
###### <comment of the respective post>
```

**Tasks that can be done on the dataset :**

- _Text classification_: The dataset can be modified to predict whether a post belongs to a subreddit or not.
- _Sentiment Analysis_: The comments (as well as the posts) can be analyzed whether they show a positive, neutral or negative sentiment.

**Resources that were used for getting the data :**

- [Source code](https://github.com/ishandandekar/Reddit_Post_Comment_Dataset)
- [PRAW (python reddit API wrapper)](https://github.com/praw-dev/praw)
- [Python Engineer's tutorial](https://www.youtube.com/watch?v=8VZhog5C3bU&ab_channel=PythonEngineer)

## Contribution

This project is still in its development phase.
Although this is not a conventional open-source project, if you find any errors (even a typo!) and/or want to improve something in the repository, and/or want to help document the project, feel free to create a pull request! 😄

#### TODO:

- [x] Find 10 more subreddits with populated text posts
- [x] Change limit 1->15.
- [ ] Document the project for contributions and reproducibility
- [ ] Publish dataset to kaggle
