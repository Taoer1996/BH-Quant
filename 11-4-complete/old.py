def initialize(context):
    stocks = ['SZ399305']
    context.set_universe(stocks)


def handle_data(context,o):
    for pos in context.portfolio.positions:
        o.order(pos.security, 1)
        print ('position %s have %d amount' % (pos, pos.total_amount))
    return 0
