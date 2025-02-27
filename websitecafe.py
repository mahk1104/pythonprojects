from flask import Flask, request, jsonify
import json

app = Flask(__name__)

ORDERS_FILE = "orders.json"

def load_orders():
    try:
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_orders(orders):
    with open(ORDERS_FILE, "w") as file:
        json.dump(orders, file, indent=4)

@app.route("/save_order", methods=["POST"])
def save_order():
    new_orders = request.json
    orders = load_orders()
    orders.extend(new_orders)
    save_orders(orders)
    return jsonify({"message": "Order saved successfully!"})

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = load_orders()
    return jsonify(orders)

if __name__ == "__main__":
    app.run(debug=True)
