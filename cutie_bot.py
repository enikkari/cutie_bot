from call_apis import get_subreddit_top_post, post_to_flowdock
import logging
import random

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

subreddits = ["RarePuppers",
              "SupermodelCats",
              "awwducational",
              "corgi",
              "PartyParrot",
              "TheCatTrapIsWorking",
              "Catloaf",
              "eyebleach",
              "Otters"
              ]


def send_message(flowdock_token, flow_token, bot_name="cutiebot"):
    try:
        subreddit = random.choice(subreddits)
        result = get_subreddit_top_post(subreddit=subreddit,
                                        user_agent=bot_name)
        title = result.get('title')
        link = result.get('url')
        message = f"Look at this cutie:\n \"{title}\"\n {link}"

        post_to_flowdock(flowdock_token,
                         flow_token,
                         bot_name,
                         message,
                         tag=subreddit)
    except BaseException as e:
        logger.info(e)
