import pandas as pd
from unittest import TestCase

class TestPandasStock(TestCase):
    """
    This class is used to test the performance of pandas
    in basic stock data operation
    """

    #Test the file can be read correctly
    def testReadFile(self):
        file_name='./demo.csv'
        df=pd.read_csv(file_name)

        print(df.info())
        print('----------------')
        print(df.describe())

    #Datetime manipulation
    def testTime(self):
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','close','open','high','low','volume']

        df['date']=pd.to_datetime(df['date'])

        df['year']=df['date'].dt.year
        df['month']=df['date'].dt.month

        print(df)

    #Find minimum close price
    def testCloseMin(self):
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','close','open','high','low','volume']

        print(f'close min : {df['close'].min()}')
        print(f'close min index : {df['close'].idxmin()}')
        print(f'close min frame : {df.loc[df['close'].idxmin()]}')

    #Calculate average monthly open and close prices
    def testMean(self):
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','close','open','high','low','volume']

        df['date']=pd.to_datetime(df['date'])
        df['month']=df['date'].dt.month

        print(f'month close mean : {df.groupby('month')['close'].mean()}')
        print(f'month open average : {df.groupby('month')['open'].mean()}')

    #Calculate daily returns
    def testRipples_ratio(self):
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','close','open','high','low','volume']

        df['date']=pd.to_datetime(df['date'])

        df['rise']=df['close'].diff()
        df['rise_ratio']=df['rise']/df.shift(1)['close']

        print(df)