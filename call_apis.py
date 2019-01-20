import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


def get_r_aww():
    url = "https://www.reddit.com/r/aww/top.json"

    response = requests.get(url)
    logger.info(response.text)

    return response.json()["data"]["children"][0]["data"]


def post_to_flowdock(flowdock_token, flow_token, bot_name, message):
    url = f"https://{flowdock_token}@api.flowdock.com/messages/chat/{flow_token}"

    payload = \
        {"external_user_name": bot_name,
         "content": f"{message}",
         "tags": "productivity"}
    headers = {
        'content-type': "application/json"
    }

    requests.post(url, json=payload, headers=headers)
