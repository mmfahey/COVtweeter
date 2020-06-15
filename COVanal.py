'''
Analysis of COVID-19 data

This module is only used with tweeter.py and is no longer being updated.
All plots are generated using JHU github repository data that is imported
into a pandas DataFrame and plotted with matplotlib to create image files
that are tweeted daily by tweeter.py in the package.
'''
import datetime as dt
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

casesData = Path('/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deathsData = Path('/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

#time confirmed data = tCD, time death data = tDD, from JHU: https://github.com/CSSEGISandData/COVID-19
tCD = pd.read_csv(casesData)
tDD = pd.read_csv(deathsData)

#create time variables
yesterday = dt.date.today() - dt.timedelta(days=1)
otherday = dt.date.today() - dt.timedelta(days=2)

#Creates the data used for tables containing top 10 countries with largest total deaths and cases
tCD['Total Confirmed Cases'] = tCD[yesterday.strftime('%#m/%#d/%y')] 
tDD['Total Deaths'] = tDD[yesterday.strftime('%#m/%#d/%y')] 
tCD['24 hour change'] = tCD[yesterday.strftime('%#m/%#d/%y')] - tCD[otherday.strftime('%#m/%#d/%y')]
tDD['24 hour change'] = tDD[yesterday.strftime('%#m/%#d/%y')] - tDD[otherday.strftime('%#m/%#d/%y')]
top10CD = tCD.nlargest(10, 'Total Confirmed Cases')
top10DD = tDD.nlargest(10, 'Total Deaths')
top10CD['24 hour change'] = top10CD[yesterday.strftime('%#m/%#d/%y')] - top10CD[otherday.strftime('%#m/%#d/%y')]
top10DD['24 hour change'] = top10DD[yesterday.strftime('%#m/%#d/%y')] - top10DD[otherday.strftime('%#m/%#d/%y')]
newtop10CD = top10CD[['Country/Region', 'Total Confirmed Cases', '24 hour change']]
newtop10DD = top10DD[['Country/Region', 'Total Deaths', '24 hour change']]

#Creates the data used for tables containing top 10 changes in countries deaths and cases
top10changeCD = tCD.nlargest(10, '24 hour change')
top10changeDD = tDD.nlargest(10, '24 hour change')
newtop10changeCD = top10changeCD[['Country/Region', 'Total Confirmed Cases', '24 hour change']]
newtop10changeDD = top10changeDD[['Country/Region', 'Total Deaths', '24 hour change']]

#Create dataframes for the global total graphs
deathtotals = tDD.sum(axis=0)
deathtotal = deathtotals[3:]
casestotals = tCD.sum(axis=0)
casestotal = casestotals[3:]

#Create dataframes for the US total graphs
USdeaths = tDD.loc[225][4:]
UScases = tCD.loc[225][4:]

def create_daily_top_10_tables():
    '''
    Creates COVID-19 tables sorted by largest total cases or deaths
    '''
    fig, axs = plt.subplots(2, 1)
    
    axs[0].set_title('Countries With Most Confirmed COVID Cases',pad=10)
    axs[0].axis('off')
    axs[0].axis('tight')
    axs[0].table(cellText=newtop10CD.values, colLabels=newtop10CD.columns, loc='center')
    
    axs[1].set_title('Countries With Most COVID Deaths (All-time)', pad=10)
    axs[1].axis('off')
    axs[1].axis('tight')
    axs[1].table(cellText=newtop10DD.values, colLabels=newtop10DD.columns, loc='center')
    fig.tight_layout(pad=2)
    plt.savefig(dt.date.today().strftime('%m%d%y') + 'total.png')

def create_daily_top_10_changes_tables():
    '''
    Creates COVID-19 tables sorted by daily (24 hr) highs in deaths or cases
    '''
    fig, axs = plt.subplots(2, 1)

    axs[0].set_title('Countries With Largest Change in Confirmed COVID Cases (24 hours)', pad=10)
    axs[0].axis('off')
    axs[0].axis('tight')
    axs[0].table(cellText=newtop10CD.values, colLabels=newtop10changeCD.columns, loc='center')
    
    axs[1].set_title('Countries With Most COVID Deaths (24 hours)', pad=10)
    axs[1].axis('off')
    axs[1].axis('tight')
    axs[1].table(cellText=newtop10DD.values, colLabels=newtop10changeDD.columns, loc='center')
    fig.tight_layout(pad=2)
    plt.savefig(dt.date.today().strftime('%m%d%y') + 'daily.png')

def create_daily_totals_graphs():
    '''
    Creates graphs of global total cases and deaths
    '''
    fig, axs = plt.subplots(2,1)

    axs[0].plot(deathtotal)
    axs[0].set_title('Total Worldwide Deaths', pad=10)
    axs[0].xaxis.set_major_locator(plt.MaxNLocator(4))
    axs[0].set(xlabel = 'Date', ylabel = 'Deaths')
    axs[0].set_xlim('1/22/20', yesterday.strftime('%#m/%#d/%y'))

    axs[1].plot(casestotal)
    axs[1].set_title('Total Worldwide Cases', pad=10)
    axs[1].xaxis.set_major_locator(plt.MaxNLocator(4))
    axs[1].set(xlabel = 'Date', ylabel = 'Cases')
    axs[1].set_xlim('1/22/20', yesterday.strftime('%#m/%#d/%y'))
    fig.tight_layout(pad=2)
    plt.savefig(dt.date.today().strftime('%m%d%y') + 'dailytotalgraph.png')

def create_daily_US_graphs():
    '''
    Creates graphs of global total cases and deaths
    '''
    fig, axs = plt.subplots(2,1)

    axs[0].plot(USdeaths)
    axs[0].set_title('Total US Deaths', pad=10)
    axs[0].xaxis.set_major_locator(plt.MaxNLocator(4))
    axs[0].set(xlabel = 'Date', ylabel = 'Deaths')
    axs[0].set_xlim('1/22/20', yesterday.strftime('%#m/%#d/%y'))

    axs[1].plot(UScases)
    axs[1].set_title('Total US Cases', pad=10)
    axs[1].xaxis.set_major_locator(plt.MaxNLocator(4))
    axs[1].set(xlabel = 'Date', ylabel = 'Cases')
    axs[1].set_xlim('1/22/20', yesterday.strftime('%#m/%#d/%y'))
    fig.tight_layout(pad=2)
    plt.savefig(dt.date.today().strftime('%m%d%y') + 'dailyUSgraph.png')
