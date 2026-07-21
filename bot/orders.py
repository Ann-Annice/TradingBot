from binance.enums import *
from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order.
    """
    try:
        logger.info(f"MARKET Order -> {side} {quantity} {symbol}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(order)
        return order

    except Exception as e:
        logger.error(e)
        raise


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order.
    """
    try:
        logger.info(f"LIMIT Order -> {side} {quantity} {symbol} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )

        logger.info(order)
        return order

    except Exception as e:
        logger.error(e)
        raise