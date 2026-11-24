#this program is run in JoinQuant's environment
#a simple program to help me familiar with the structure of quant programming
def initialize(context):
    '''
    initialize the parameters of trading
    g is a JoinQuant's global variable that use to store the stock id
    '''
    g.security='000001.XSHE'
    run_daily(market_open,time='every_bar')
    #set benchmark as another bank
    set_benchmark('600000.XSHG')
    #set commission/stamp duty
    set_order_cost(OrderCost(open_commission=0.03,close_commission=0.03,
    close_tax=0.001,min_commission=5),type='stock')
    #set slippage
    set_slippage(PriceRelatedSlippage(0.002),type='stock')
    #set volume ratio
    set_option('order_volume_ratio',0.5)
    #set dynamic price adjustment mode
    set_option('use_real_price',True)


def market_open(context):
    '''
    buy when current price is 1% over MA5
    sell when current price is under MA5
    '''
    security = g.security
    close_data = attribute_history(security, 5, '1d', ['close'])
    MA5 = close_data['close'].mean()
    current_price = close_data['close'][-1]

    cash = context.portfolio.available_cash

    if current_price > 1.01 * MA5:
        order_value(security, cash)
        log.info(f'buy {security}')

    elif current_price < MA5 and context.portfolio.positions[security].closeable_amount > 0:
        order_value(security, 0)
        log.info(f'sell {security}')

    record(stock_price=current_price)