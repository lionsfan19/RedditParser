import praw


reddit = praw.Reddit(client_id = '', 
                     client_secret = '' ,
                     username = '' ,
                     password = '!' ,
                     user_agent = '',
                     get_submission = '')

subreddit = reddit.subreddit('roastme')

hot_python = subreddit.hot(limit=5)
for submission in hot_python:
    print(submission.title)



    
    
comments = submission.comments

for comment in comments:
        print(20*'-')
        print(comment.body)
    
