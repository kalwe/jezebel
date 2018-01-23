# TODO: add fees in both methodos
# cath fees from exchange and order type
""" Return a percent from a value """
def calc_prt(value, percent):
    return value * (percent /100)

""" Return a value to gain with base in a percent argument """
def profit_to_gain(price, percent2gain, fee):
    return price + (calc_prt(price, percent2gain) + calc_prt(price, fee))

def profit_to_loss(price, percent2loss, fee):
    return price - (calc_prt(price, percent2loss) + calc_prt(price, fee))

def profit_gain_without_fees(price, percent2gain):
    return profit_to_gain(price, percent2gain, 0)

def profit_loss_without_fees(price, percent2loss):
    return profit_to_loss(price, percent2loss, 0)

def profit_one_prct(price, fee):
    return profit_to_gain(price, 1, fee)

# JUST TO TEST
# print("ZERO -", profit_to_gain(100, 0, 0.4))
# print("GAIN -", profit_to_gain(100, 1, 0.4))
# print("LOSS -", profit_to_loss(100, 0.33, 0.4))
# print("GAIN WITHOUT FEES - ", profit_gain_without_fees(100, 1))
# print("LOSS WITHOUT FEES - ", profit_loss_without_fees(100, 1))
