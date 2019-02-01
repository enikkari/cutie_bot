import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


def get_subreddit_top_post(subreddit="aww", user_agent=""):
    url = f"https://www.reddit.com/r/{subreddit}/top.json"

    response = requests.get(url, headers={"User-Agent": user_agent})

    resp_data = response.json()["data"]["children"][0]["data"]
    return {'url': f"https://www.reddit.com/{resp_data['permalink']}", 'title': resp_data['title']}


def post_to_flowdock(flowdock_token, flow_token, bot_name, message, tag="productivity"):
    url = f"https://{flowdock_token}@api.flowdock.com/messages/chat/{flow_token}"

    payload = \
        {"external_user_name": bot_name,
         "content": f"{message}",
         "tags": tag}
    headers = {
        'content-type': "application/json"
    }

    requests.post(url, json=payload, headers=headers)
