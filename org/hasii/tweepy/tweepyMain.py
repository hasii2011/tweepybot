
from typing import List

import json

import logging
import logging.config

import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy.error import TweepError

from tweepy import Status

API_KEY             = "PUT YOUR API KEY HERE"
API_SECRET_KEY      = "PUT YOUR SECRET KEY HERE"
ACCESS_TOKEN        = "PUT YOUR ACCESS TOKEN HERE"
ACCESS_TOKEN_SECRET = "PUT YOUR TOKEN SECRET HERE"

JSON_LOGGING_CONFIG_FILENAME = "loggingConfiguration.json"


def main():

    with open(JSON_LOGGING_CONFIG_FILENAME, 'r') as loggingConfigurationFile:
        configurationDictionary = json.load(loggingConfigurationFile)

    logging.config.dictConfig(configurationDictionary)
    logging.logProcesses = False
    logging.logThreads = False

    logger = logging.getLogger(__name__)

    logger.info(f"I am a tweepy bot")

    # Authenticate to Twitter
    auth: OAuthHandler = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api: API = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        logger.info("Authentication OK")

        timeline: List[Status] = api.home_timeline()
        logger.info(f"Last 20 tweets --------------------------------")
        for tweet in timeline:
            logger.info(f"{tweet.user.name} said {tweet.text}")

        logger.info(f"Mentions -------------------------------")
        tweets: List[Status] = api.mentions_timeline()
        for tweet in tweets:
            logger.info(f"User: {tweet.user.name} mentioned me: {tweet.text}")

    except TweepError as ex:
        logger.exception(f"Error during authentication:  {ex}")


if __name__ == "__main__":
    main()
