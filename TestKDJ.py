import pandas as pd
import matplotlib.pyplot as plt

from unittest import TestCase

class TestKDJ(TestCase):

    """
    This class is used to test the performances of pandas and
    matplotlib.pyplot in calculating and plotting KDJ
    """

    def cal_kdj(self,df):
        '''
        Calculate the k,d,j values of given dataframe df
        return dataframe with kdj values
        '''
        low_list=df['low'].rolling(9,min_periods=9).min()
        low_list=low_list.fillna(value=df['low'].expanding().min())
        high_list=df['high'].rolling(9,min_periods=9).max()
        high_list=high_list.fillna(value=df['high'].expanding().max())
        rsv=(df['close']-low_list)/(high_list-low_list)*100
        df['k']=pd.DataFrame(rsv).ewm(com=2).mean()
        df['d']=df['k'].ewm(com=2).mean()
        df['j']=3*df['k']-2*df['d']
        return df

    def test_KDJ(self):
        '''
        initialise dateframe then call cal_kdj and plot kdj diagram
        '''
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','close','open','high','low','volume']
        df=df[['date','close','open','high','low','volume']]
        df['date']=pd.to_datetime(df['date'])

        df=self.cal_kdj(df)
        print(df)

        df = df.set_index('date')

        plt.figure()
        df['k'].plot(color='red',label='k')
        df['d'].plot(color='yellow',label='d')
        df['j'].plot(color='blue', label='j')
        plt.legend(loc='best')


        plt.grid(linestyle='-.')
        plt.title('000001 KDJ diagram')
        plt.show()
