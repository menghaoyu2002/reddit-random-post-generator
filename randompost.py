import praw
import random
from requests import Session
import webbrowser

class RandomPost:
    subreddits: list

    def __init__(self) -> None:
        session = Session()
        reddit = praw.Reddit(client_id="mfTh5fVtdcpbHQ",
                            client_secret="HnqZzByPo93VLGDihr-mOpgOoNh5VQ",
                            requestor_kwargs={"session": session},  # pass Session
                            redirect_uri="http://www.example.com/unused/redirect/uri",
                            user_agent="Grab and Dash by u/6e-6f-74-61-62-6f-74",
                            username="6e-6f-74-61-62-6f-74")

        memes_sub = reddit.subreddit("memes")
        make_me_suffer_sub = reddit.subreddit("MakeMeSuffer")
        cringe_sub = reddit.subreddit("Cringetopia")
        tiktok_sub = reddit.subreddit("TikTokCringe")

        self.subreddits = [memes_sub, make_me_suffer_sub, cringe_sub, tiktok_sub]

    def get_random_post(self) -> None:
        print('opening new tab')
        subreddit = random.choice(self.subreddits)
        post_number = random.randint(0, 99)
        i = 0
        for post in subreddit.hot():
            if i == post_number:
                webbrowser.open(post.url)
                return
            i += 1

