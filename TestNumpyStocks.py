import numpy as np
from unittest import TestCase

class TestNumpyStock(TestCase):
    """
    This class is used to test the performance of numpy
    in basic stock data operation

    fname: str, the name of the file
    delimiter: str, the string used to separate values
    usecols: tuple, the reciprocal of read data, which columns to read, with 0 being the first
    unpack: bool, whether to unpack the columns into separate arrays
    """

    #Test the file can be read correctly
    def testReadFile(self):
        file_name='./demo.csv'
        end_price,volume=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,6),
            unpack=True
        )
        print(end_price)
        print(volume)

    #Find the Maximum value and Minimum value
    def testMaxAndMin(self):
        file_name = './demo.csv'
        high_price,low_price=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(4,5),
            unpack=True
        )
        print(f'max price = {high_price.max()}')
        print(f'min price = {low_price.min()}')

    #Range
    #Calculate the difference between the maximum and minimum values of recent max price and min price
    def testPtp(self):
        file_name = './demo.csv'
        high_price,low_price=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(4,5),
            unpack=True
        )
        print(f'range of max price = {np.ptp(high_price):.2f}')
        print(f'range of min price = {np.ptp(low_price):.2f}')

    #Calculate VWAP(Volume-Weighted Average Price)
    def testAVG(self):
        file_name = './demo.csv'
        end_price,volume=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,6),
            unpack=True
        )
        print(f'average price = {np.average(end_price)}')
        print(f'VWAP = {np.average(end_price,weights=volume)}')

    #Find the medium of end price
    def testMedian(self):
        file_name = './demo.csv'
        end_price=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,),
            unpack=True
        )
        print(f'medium = {np.median(end_price):f}')

    #Find the variance of end price
    def testVar(self):
        file_name = './demo.csv'
        end_price=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,),
            unpack=True
        )
        print(f'variance = {np.var(end_price)}')

    #Calculate stock returns, annual volatility, and monthly volatility
    def testVolatility(self):
        file_name = './demo.csv'
        end_price,volume=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,6),
            unpack=True
        )

        log_return=np.diff(np.log(end_price))

        annual_volatility=log_return.std() * np.sqrt(250)

        monthly_volatility = log_return.std() * np.sqrt(21)

        print(f'log return = {log_return}')
        print(f'annual volatility = {annual_volatility:.2%}')
        print(f'monthly volatility = {monthly_volatility:.2%}')
