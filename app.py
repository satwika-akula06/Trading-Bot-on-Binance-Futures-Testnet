import streamlit as st
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()
st.set_page_config(page_title="Trading Bot", layout="centered")

st.title(" Binance Trading Bot (Testnet)")
st.write("Place MARKET, LIMIT and STOP-LIMIT orders")

# Inputs
symbol = st.selectbox("Select Symbol", ["BTCUSDT", "ETHUSDT", "BNBUSDT"])
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0)

price = None
stop_price = None

if order_type in ["LIMIT", "STOP_LIMIT"]:
    price = st.number_input("Limit Price", min_value=0.0)

if order_type == "STOP_LIMIT":
    stop_price = st.number_input("Stop Price", min_value=0.0)

# Button
if st.button(" Place Order"):
    try:
        validate_order(side, order_type, quantity, price, stop_price)

        order = place_order(
            symbol,
            side,
            order_type,
            quantity,
            price,
            stop_price
        )

        st.success(" Order Placed Successfully!")

        st.write("### Order Details")
        st.write(f"Order ID: {order['orderId']}")
        st.write(f"Status: {order['status']}")
        st.write(f"Executed Qty: {order['executedQty']}")
        st.write(f"Avg Price: {order.get('avgPrice')}")

        if order_type == "STOP_LIMIT":
            st.write(f"Stop Price: {stop_price}")

    except Exception as e:
        st.error(f" Error: {str(e)}")