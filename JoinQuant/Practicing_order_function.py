# this program is run in JoinQuant's environment
# Practicing order functions
def initialize(context):
    # Set benchmark as '000300.XSHG'
    set_benchmark('000300.XSHG')
    g.security = '000001.XSHE'
    run_daily(market_open, time='9:30')
    run_daily(after_market_close, time='15:30')


def market_open(context):
    # Deposit 10000
    inout_cash(10000, pindex=0)
    # Get cash remain
    log.info(f'available cash {context.portfolio.subportfolios[0].available_cash}')

    # If no position is held
    if g.security not in context.portfolio.positions:
        # Order 1000 shares
        order(g.security, 1000)
    else:
        # Sell 500 shares
        order(g.security, -500)


def after_market_close(context):
    # Get all open orders for today
    orders = get_open_orders()
    for _order in orders:
        log.info(f'open orders {_order}')
    # Cancel all open orders
    for _order in orders:
        cancel_order(_order)
        log.info(f'open orders {_order}')