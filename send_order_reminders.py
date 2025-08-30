import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

endpoint = "http://localhost:8000/graphql"
transport = RequestsHTTPTransport(url=endpoint, verify=False)
client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql("""
query GetRecentOrders {
  orders(orderDateWithinDays: 7) {
    id
    customer {
      email
    }
  }
}
""")

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("/tmp/order_reminders_log.txt", "a") as f:
    try:
        result = client.execute(query)
        for order in result["orders"]:
            f.write(f"{now} - Order {order['id']} for {order['customer']['email']}\n")
        print("Order reminders processed!")
    except Exception as e:
        f.write(f"{now} - ERROR: {str(e)}\n")
