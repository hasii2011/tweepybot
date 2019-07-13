
import os

from logging import getLogger
from logging import Logger

from tweepy import OAuthHandler
from tweepy import API
from tweepy.error import TweepError

logger: Logger = getLogger()


def create_api():

    consumer_key:        str = os.getenv("CONSUMER_KEY")
    consumer_secret:     str = os.getenv("CONSUMER_SECRET")
    access_token:        str = os.getenv("ACCESS_TOKEN")
    access_token_secret: str = os.getenv("ACCESS_TOKEN_SECRET")

    auth: OAuthHandler = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api: API = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()

    except TweepError as ex:
        logger.error("Error during authentication:  {ex}", exc_info=True)
        raise ex

    logger.info("API created")
    return api
