import argparse
import logging
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger

# 🔑 PUT YOUR API KEYS HERE
API_KEY = "lnViGqmHItidP7xoz4MnZmaYeQXO6M5OVp7HXjnpEbFOyES1Un6TOtmVq1WJDzVW"
API_SECRET = "8vJJVDS0RInlZmyv4MrTpLzRY0DHpmngCG7TFB5aFz8uPe0GEbDq1VqpSj3I6yme"


def main():
    # ✅ Start logging
    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        # ✅ Validate input
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        # ✅ Create Binance client
        client = BinanceClient(API_KEY, API_SECRET).get_client()

        # ✅ Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # ✅ Clean output
        print("\n✅ Order placed successfully")
        print("Symbol:", order.get("symbol"))
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Side:", order.get("side"))
        print("Type:", order.get("type"))

        # ✅ Log success
        logging.info(f"SUCCESS: {order}")

    except Exception as e:
        print("\n❌ Error:", str(e))
        logging.error(f"ERROR: {str(e)}")


if __name__ == "__main__":
    main()