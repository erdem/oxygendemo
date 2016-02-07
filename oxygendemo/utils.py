from oxygendemo.constants import GPB_TO_USD_RATE, GPB_TO_EUR_RATE


def convert_gpb_to_usd(gpb_price):
    if not gpb_price is float:
        gpb_price = float(gpb_price)
    return gpb_price * GPB_TO_USD_RATE


def convert_gpb_to_eur(gpb_price):
    if not gpb_price is float:
        gpb_price = float(gpb_price)
    return gpb_price * GPB_TO_EUR_RATE
