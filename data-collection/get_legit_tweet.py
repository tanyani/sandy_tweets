#!/usr/bin/python

import tweepy
import json
import csv
import pandas as pd
import sys

with open('/home/cusp/tn1050/twitter.config') as jf:
    auth = json.load(jf)

authe = tweepy.OAuthHandler(auth['twitter']['CONSUMER_API_KEY'], auth['twitter']['CONSUMER_API_SECRET_KEY'])
authe.set_access_token(auth['twitter']['ACCESS_TOKEN'], auth['twitter']['ACCESS_TOKEN_SECRET'])

df = pd.read_csv(sys.argv[1], sep='\t', names=['tid', 'uid', 'md5'])
df.drop('md5', axis=1)
api = tweepy.API(authe, wait_on_rate_limit=True)

counter = 0
# tweets = []


with open(sys.argv[2], 'w') as fl, open(sys.argv[3], 'w') as fl_geo:
    for idx, row in df.iterrows():
        print('%d/%d (%f) |' % (counter, df.shape[0], (counter/df.shape[0])))
        counter += 1
        try:
            tweet = api.get_status(row[0])
            geo = str(tweet.geo) if tweet.geo != None else ''

            res = [str(row[0]), str(row[1]), str(tweet.created_at), geo, str(tweet.text)]
            # print(','.join("'{0}'".format(x) for x in res))
            if len(geo) >= 2:
                fl_geo.write(','.join("'{0}'".format(x) for x in res)+'\n')
            # tweets.append(res)
            fl.write(','.join("'{0}'".format(x) for x in res)+'\n')
        except Exception as e:
            print('### DIU', e)
            continue

# fl.close()
# fl_geo.close()
