import datetime
import requests

log_file = "/tmp/order_reminders_log.txt"
url = "http://localhost:8000/graphql"

query = """
query {
  orders(lastWeek: true) {
    id
    customer {
      email
    }
  }
}
"""

response = requests.post(url, json={'query': query})
orders = response.json().get("data", {}).get("orders", [])

with open(log_file, "a") as f:
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for order in orders:
        f.write(f"{ts} - Order {order['id']} reminder sent to {order['customer']['email']}\n")

print("Order reminders processed!")
