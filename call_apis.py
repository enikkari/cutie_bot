import requests
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
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
    logger.info(payload)
    logger.info(headers)

    requests.post(url, json=payload, headers=headers)

if __name__ == '__main__':
    flowdock_token = os.environ["FLOWDOCK_TOKEN"]
    flow_token = os.environ["FLOW_TOKEN"]
    bot_name = os.environ["BOT_NAME"]

    result = get_r_aww()
    title = result.get('title')
    link = result.get('url')

    message = f'Look at this cutie:\n "{title}"\n {link}'

    post_to_flowdock(flow_token,
                     flow_token,
                     bot_name,
                     message)
