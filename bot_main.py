import os
from call_apis import get_r_aww, post_to_flowdock
import schedule, time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


def main():
    flowdock_token = os.environ["FLOWDOCK_TOKEN"]
    flow_token = os.environ["FLOW_TOKEN"]
    bot_name = os.environ["BOT_NAME"]
    logger.info(f'main()')

    try:
        result = get_r_aww(user_agent=bot_name)
        title = result.get('title')
        link = result.get('url')
        message = f'Look at this cutie:\n "{title}"\n {link}'

        post_to_flowdock(flowdock_token,
                         flow_token,
                         bot_name,
                         message)
    except BaseException as e:
        logger.info(e)


if __name__ == '__main__':
    run_at = "10:02"
    logger.info(f'Running time: {run_at}')
    schedule.every().day.at(run_at).do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
