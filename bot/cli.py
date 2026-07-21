import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "MARKET":
            response = place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
            )
        else:
            price = validate_price(args.price)

            print(f"Price    : {price}")

            response = place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Average Price : {response.get('avgPrice')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print("\n❌ Error:")
        print(e)


if __name__ == "__main__":
    main()