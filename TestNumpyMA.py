import numpy as np
import matplotlib.pyplot as plt

from unittest import TestCase

class TestNumpyMA(TestCase):


    #Calculate 5-day SMA(Simple Moving Average)
    def testSMA(self):
        file_name='./demo.csv'
        end_price=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,),
            unpack=True
        )
        print(end_price)
        N=5
        weights=np.ones(N)/N
        print(weights)
        sma=np.convolve(weights,end_price)[N-1:-N+1]
        print(sma)
        plt.figure()
        plt.plot(sma,linewidth=5)
        plt.show()



    #Calculate 5-day EMA(Exponential Moving Average)
    def testEMA(self):
        file_name='./demo.csv'
        end_price=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,),
            unpack=True
        )
        print(end_price)
        N=5
        weights=np.exp(np.linspace(0,-1,N))
        weights/=weights.sum()
        print(weights)
        ema=np.convolve(weights,end_price)[N-1:-N+1]
        print(ema)

        t=np.arange(N-1,len(end_price))
        plt.figure()
        plt.plot(t,end_price[N-1:],lw=1.0,label='end price')
        plt.plot(t,ema,lw=2.0,label='ema')
        plt.legend(loc='best')
        plt.show()