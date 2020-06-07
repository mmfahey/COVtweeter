'''
Module Docstring
'''
import os
import datetime as dt

import tweepy

import COVanal as CV

#twitter API settings, this are from the user's twitter developer account
consumer_key = os.environ.get('COVID_CONSUMER_KEY') 
consumer_secret = os.environ.get('COVID_CONSUMER_SECRET')
access_token = os.environ.get('COVID_ACCESS_TOKEN')
access_token_secret = os.environ.get('COVID_ACCESS_TOKEN_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def dailytweets():
    '''Twitterbot that publishes COVID-19 data

    Meant to be run once a day that runs COVID data analysis modules 
    and then posts the results as tweets. It also deletes the files
    following creation.
    '''

    #Runs the functions from the COVanal module to generate the tables and graphs to be published
    CV.create_daily_top_10_tables()
    CV.create_daily_top_10_changes_tables()
    CV.create_daily_totals_graphs()
    CV.create_daily_US_graphs()
    #Tweet 1 - file to be tweeted, actual tweet with text, delete figure
    tweettopublish1 = dt.date.today().strftime('%m%d%y') + 'total.png'
    api.update_with_media(tweettopublish1, f'COVID-19 Global Top 10 totals ({dt.date.today()}) #COVID #COV #Data #CoronaVirus')
    os.remove(dt.date.today().strftime('%m%d%y') + 'total.png')
    #Tweet 2 - file to be tweeted, actual tweet with text, delete figure
    tweettopublish2 = dt.date.today().strftime('%m%d%y') + 'daily.png'
    api.update_with_media(tweettopublish2, f'COVID-19 Global Top 10 changes over 24 hours ({dt.date.today()}) #COVID #COV #Data #CoronaVirus')
    os.remove(dt.date.today().strftime('%m%d%y') + 'daily.png')
    #Tweet 3 - file to be tweeted, actual tweet with text, delete figure
    tweettopublish3 = dt.date.today().strftime('%m%d%y') + 'dailytotalgraph.png'
    api.update_with_media(tweettopublish3, f'COVID-19 Global Total Graphs ({dt.date.today()}) #COVID #COV #Data #CoronaVirus')
    os.remove(dt.date.today().strftime('%m%d%y') + 'dailytotalgraph.png')
    #Tweet 4 - file to be tweeted, actual tweet with text, delete figure
    tweettopublish4 = dt.date.today().strftime('%m%d%y') + 'dailyUSgraph.png'
    api.update_with_media(tweettopublish4, f'COVID-19 US Total Graphs ({dt.date.today()}) #COVID #COV #Data #CoronaVirus')
    os.remove(dt.date.today().strftime('%m%d%y') + 'dailyUSgraph.png')

def main():
    dailytweets()

if __name__ == '__main__':
    main()