# this program is run in JoinQuant's environment
# time function
def initialize(context):
    # Set benchmark as '000300.XSHG'
    set_benchmark('000300.XSHG')
    g.security = '000001.XSHE'
    # run daily, every minute
    # run_daily(market_open,time='every_bar',reference_security='000300.XSHG')
    # run monthly, at the start of the month
    # run_monthly(market_open,1,time='open')
    # run weekly, at the end of the week
    run_weekly(market_open, -1, time='open')


def market_open(context):
    if g.security not in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)