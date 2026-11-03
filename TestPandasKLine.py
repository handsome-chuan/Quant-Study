import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from unittest import TestCase

class TestPandasKLine(TestCase):
    """
    This class is used to test the performance of pandas
    in plotting K-Line, volume and SMA
    """

    #Plot K-Line with volume
    def testKLineChart(self):
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','Close','Open','High','Low','Volume']
        df['date']=pd.to_datetime(df['date'])
        df=df.set_index('date')

        my_color = mpf.make_marketcolors(
            up='green',
            down='red',
            edge='inherit',
            wick='inherit',
            volume='in'
        )

        my_style = mpf.make_mpf_style(marketcolors=my_color)

        mpf.plot(df, type='candle', volume=True, title='K-Line',style=my_style)

    #Plot K-Line with volume and 5-days SMA(Simple Moving Average)
    def testKLineByMA(self):
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','Close','Open','High','Low','Volume']
        df['date']=pd.to_datetime(df['date'])
        df=df.set_index('date')

        my_color = mpf.make_marketcolors(
            up='green',
            down='red',
            edge='inherit',
            wick='inherit',
            volume='in'
        )

        my_style = mpf.make_mpf_style(marketcolors=my_color,gridstyle='-.',gridcolor='lightgray')

        mpf.plot(df, type='candle', volume=True, title='K-Line with SMA',style=my_style,mav=(5,10),mavcolors=['blue','orange'])