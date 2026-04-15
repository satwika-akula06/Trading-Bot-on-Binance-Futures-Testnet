import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)
parser.add_argument("--stop_price", type=float)

args = parser.parse_args()

try:
    validate_order(args.side, args.type, args.quantity, args.price, args.stop_price)

    print("\n Order Summary :")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.price:
        print(f"Price: {args.price}")

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price,
        args.stop_price
    )

    print("\n Order Successful!")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])
    print("Executed Qty:", order["executedQty"])
    print("Avg Price:", order.get("avgPrice"))

except Exception as e:
    print("\n Error:", str(e))