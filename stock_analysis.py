#pip install yfinance
#pip install pandas
#pip install matplotlib
#pip install python-pptx

import yfinance as yf
import pandas as pd
import matplotlib
from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches

cisco = yf.Ticker("CSCO")

# Defining objects with key information about the company

cisco_info = cisco.info  # dict with key company info
# print(cisco_info['currentPrice'])
# print(cisco_info.keys())

cisco_share_price_data = cisco.history(period="max")
# print(cisco_share_price_data.head())

#cisco_share_price_data.reset_index(inplace=True)
#cisco_share_price_data.plot(x="Date", y="Open")


cisco_dividend_data = cisco.dividends
print(cisco_dividend_data.head())


