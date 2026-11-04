import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unittest import TestCase



class TestMACD(TestCase):
    """
    This class is used to test the performances of pandas and
    matplotlib.pyplot in calculating and plotting MACD
    """
    def cal_macd(self,df,fastperiod=12,slowperiod=26,signalperiod=9):
        """
        calculate ema(12), ema(26), then find out DIF, DEA and MACD (bar)
        """
        ewma12=df['close'].ewm(span=fastperiod,adjust=False).mean()
        ewma26=df['close'].ewm(span=slowperiod,adjust=False).mean()
        df['dif']=ewma12-ewma26
        df['dea']=df['dif'].ewm(span=signalperiod,adjust=False).mean()
        df['bar']=(df['dif']-df['dea'])*2
        return df

    def test_MACD(self):
        """
        plot MACD by using pandas and matplotlib.pyplot
        """
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','close','open','high','low','volume']
        df=df[['date','close','open','high','low','volume']]
        df['date']=pd.to_datetime(df['date'])

        df_macd=self.cal_macd(df)
        print(df_macd)

        plt.figure()
        df_macd['dea'].plot(color='red',label='dea')
        df_macd['dif'].plot(color='blue',label='dif')
        plt.legend(loc='best')

        positive_bar=[]
        positive_index=[]
        negative_bar=[]
        negative_index=[]

        for index,row in df_macd.iterrows():
            if row['bar']>0:
                positive_bar.append(row['bar'])
                positive_index.append(index)
            else:
                negative_bar.append(row['bar'])
                negative_index.append(index)

        plt.bar(positive_index,positive_bar,width=0.5,color='red')
        plt.bar(negative_index,negative_bar,width=0.5,color='green')
        major_index=df_macd.index[df_macd.index]
        major_xtics=df_macd['date'][df_macd.index]
        plt.xticks(major_index,major_xtics)
        plt.setp(plt.gca().get_xticklabels(),rotation=30)

        plt.grid(linestyle='-.')
        plt.title('MACD of share code 000001.SZ')
        plt.rcParams['axes.unicode_minus']=False
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.show()

    #For loop is not efficient at all, maybe numby could perform better in this case
    def test_Numpy_MACD(self):
        """
        change the for loop into np.where, which is a vectorised 'if...else...' statement
        it saves some time (negligible), may due to the amount of data
        """
        file_name='./demo.csv'
        df=pd.read_csv(file_name)
        df.columns=['stock_id','date','close','open','high','low','volume']
        df=df[['date','close','open','high','low','volume']]
        df['date']=pd.to_datetime(df['date'])

        df_macd=self.cal_macd(df)
        print(df_macd)

        plt.figure()
        df_macd['dea'].plot(color='red',label='dea')
        df_macd['dif'].plot(color='blue',label='dif')
        plt.legend(loc='best')

        colors = np.where(df_macd['bar'] > 0, 'red', 'green')

        plt.bar(df_macd.index, df_macd['bar'], width=0.5, color=colors)

        major_index=df_macd.index[df_macd.index]
        major_xtics=df_macd['date'][df_macd.index]
        plt.xticks(major_index,major_xtics)
        plt.setp(plt.gca().get_xticklabels(),rotation=30)

        plt.grid(linestyle='-.')
        plt.title('MACD of share code 000001.SZ')
        plt.rcParams['axes.unicode_minus']=False
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.show()