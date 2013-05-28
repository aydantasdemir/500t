# -*- coding: utf8 -*-

import re
import requests
import json

from django.utils.encoding import smart_unicode


def get_tweet_id(url):
    result = re.search('status/([0-9]*)', url)
    if result:
        return result.group(1)

    raise ValueError("couldn't find tweet id.")


def get_tweet(url):
    tweet = ""
    try:
        tweet_id = get_tweet_id(url)
        r = requests.get("https://api.twitter.com/1/statuses/show.json?id={0}".format(
            tweet_id
        ))

        tweet_content = json.loads(smart_unicode(r.text))

    except ValueError:
        # try to find username
        result = re.search('twitter.com/([^/]*)', url)
        if result:
            username = result.group(1)
        else:
            return None

        r = requests.get(
            "https://api.twitter.com/1/statuses/user_timeline.json?screen_name={0}&count=1".format(
                username
            )
        )

        tweet_content = json.loads(smart_unicode(r.text))[0]

    if 'user' in tweet_content:
        tweet += "[user: {0}] ".format(tweet_content.get("user").get("name").encode('utf-8'))

    if 'text' in tweet_content:
        tweet += tweet_content.get("text").encode('utf-8')
    else:
        return None

    tweet += " - [RT: {0}, FAV: {1}]".format(
        tweet_content.get("retweet_count"),
        tweet_content.get("favorite_count")
    )

    return tweet







