#!/usr/bin/env python

from logging import basicConfig
from logging import Logger
from logging import getLogger
from logging import INFO

from time import sleep

from tweepy import Cursor
from tweepy import API


from org.hasii.tweepybots.config import create_api

basicConfig(level=INFO)

logger: Logger = getLogger()


def follow_followers(api: API):

    logger.info("Retrieving and following followers")
    for follower in Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()


def main():
    api: API = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        sleep(60)


if __name__ == "__main__":
    main()
