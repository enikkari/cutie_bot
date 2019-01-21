from call_apis import get_r_aww, post_to_flowdock
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


def send_message(flowdock_token, flow_token, bot_name="cutiebot"):
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