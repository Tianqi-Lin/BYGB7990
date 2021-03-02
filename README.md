Draw a Candle Plot
=============

The python module `candle_plot.py` accomplishes the following tasks:

1. Retrieve the historical stock price and trading volume series of the stock from yahoo finance website, given the ticker.
2. Output a stock technical graph with the follow specs:
   - Topchart:
     - Candle Stick representation of the stock intra-day movement (green bar indicate stock closed higher than open, red bar for closing lower than open)
     - Overlay short moving average price line and long moving average price line
   - Bottomchart:
     - Bar chart for daily trading volume (express in unit of million shares)
