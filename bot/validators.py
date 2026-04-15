def validate_input(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")