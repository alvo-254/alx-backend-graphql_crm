#!/usr/bin/env python3
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import datetime

def main():
    # GraphQL endpoint (adjust if needed)
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql/",
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Example query: get all orders with no reminders sent
    query = gql("""
    query {
      allOrders {
        id
        customer {
          name
          email
        }
        totalAmount
      }
    }
    """)

    try:
        result = client.execute(query)
        orders = result.get("allOrders", [])
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("/tmp/order_reminders_log.txt", "a") as log:
            log.write(f"[{now}] Fetched {len(orders)} orders for reminder\n")

    except Exception as e:
        with open("/tmp/order_reminders_log.txt", "a") as log:
            log.write(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()
