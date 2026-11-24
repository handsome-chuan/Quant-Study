#This is a list of useful function in JoinQuant

#set benchmark
set_benchmark(security)
#e.g.:
set_benchmark('600000.XSHG')

#set commission/stamp duty
set_order_cost(cost,type,ref=None)
#e.g.
set_order_cost(OrderCost(open_commission=0.03, close_commission=0.03,
                         close_tax=0.001, min_commission=5), type='stock')

#set slippage
set_slippage(object,type=None,ref=None)
#e.g.
set_slippage(PriceRelatedSlippage(0.002), type='stock')

#set volume ratio
set_option('order_volume_ratio',value)
#e.g.
set_option('order_volume_ratio', 0.5)

#set dynamic price adjustment mode
set_option('use_real_price',value)
#e.g.
set_option('use_real_price',True)

# order at certain amount
order(security,amount,style=None,side='long',pindex=0)

# order at certain value
order_value(security,value,style=None,side='long',pindex=0)

# target order number
order_value(security,value,style=None,side='long',pindex=0)

# get orders
get_orders(order_id=None,security=None,status=None)

# get open orders
get_open_orders()

# cancel order
cancel_order(order)

# deposit / cash out
inout_cash(cash,pindex=0)