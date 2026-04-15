import logging
import random
import time
from bot.client import get_client, USE_MOCK

client = get_client()

def mock_order(symbol, side, order_type, quantity, price):
    return {
        "orderId": random.randint(100000, 999999),
        "status": "FILLED",
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "executedQty": quantity,
        "avgPrice": price if price else "market_price",
        "time": int(time.time())
    }

def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        logging.info(f"Request: {symbol} {side} {order_type}")

        # ✅ MOCK MODE
        if USE_MOCK:
            order = mock_order(symbol, side, order_type, quantity, price)
            order["stopPrice"] = stop_price
            logging.info(f"Mock Response: {order}")
            return order

        # ✅ REAL MODE
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        logging.info(f"Response: {order}")
        return order

    except Exception as e:
        logging.error(str(e))
        raise