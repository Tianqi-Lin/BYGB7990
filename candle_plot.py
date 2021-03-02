#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('mode.chained_assignment', None)


# In[2]:


def get_hdata_from_yahoo(ticker):
    url = 'https://finance.yahoo.com/quote/{0}/history?p={0}'.format(ticker)
    data = pd.read_html(url)
    df = data[0][:-1]
    df.drop_duplicates(subset='Date', inplace=True) # drop dividend info
    df.index = pd.to_datetime(df['Date']).apply(lambda x: x.strftime('%Y-%m-%d'))
    del df['Date']
    df = df.astype('d')
    df.columns = ['Open','High','Low','Close','AdjClose','Volume']
    df = df[::-1]
    return df


# In[3]:


def plot_candlestick(ticker, shortMAW=5, longMAW=15):
    #
    # get data
    #
    df = get_hdata_from_yahoo(ticker)
    #
    # calculate moving average
    #
    df['SMA'] = df.Close.rolling(window=shortMAW).mean()
    df['LMA'] = df.Close.rolling(window=longMAW).mean()
    #
    # customize figure layout
    #
    fig = plt.figure(figsize=(16,8))
    grid = plt.GridSpec(4,4)
    ax1 = fig.add_subplot(grid[0:3,:])
    ax2 = fig.add_subplot(grid[3,:])
    #
    # top chart (main)
    #
    x = list(range(0,df.shape[0]))
    y = (df['High'] + df['Low'])/2
    yerror = (df['High'] - df['Low']) / 2
    y2 = (df['Open'] + df['Close']) / 2
    yerror2 = (df['Open'] - df['Close']) / 2
    colors = ['r' if i>0 else 'g' for i in yerror2]
    ## plot candle sticks
    ax1.errorbar(x, y, yerror, fmt='none', ecolor='k', linewidth=1) # lines
    ax1.errorbar(x, y2, yerror2, fmt='none', ecolor=colors, linewidth=5) # boxes
    ## plot moving average price lines
    ax1.plot(x, df.SMA, label='Short Moving Average ({0} days)'.format(shortMAW))
    ax1.plot(x, df.LMA, label='Long Moving Average ({0} days)'.format(longMAW))
    ax1.legend(loc='upper left')
    ## set xticks
    ax1.set_xticks(x[::10]+[x[-1]]);
    ax1.set_xticklabels(list(df.index[::10])+[df.index[-1]]);
    #
    # bottom chart
    #
    ax2.bar(x, df['Volume']/1000000.0)
    ax2.set_xticks(x[::10]+[x[-1]]);
    ax2.set_xticklabels(list(df.index[::10])+[df.index[-1]]);
    #
    # save fig
    #
    fig.savefig('{0}_plot_{1}_{2}.png'.format(ticker,shortMAW,longMAW))


# In[4]:


plot_candlestick('AMZN')


# In[5]:


plot_candlestick('AMZN',3,10)


# In[6]:


plot_candlestick('TSLA')


# In[7]:


plot_candlestick('AAPL')


# In[ ]:




