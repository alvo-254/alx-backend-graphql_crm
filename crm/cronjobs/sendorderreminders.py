#!/usr/bin/env python3
import sys
import os
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

# GraphQL endpoint
GRAPHQL_ENDPOINT = "http://localhost:8000/graphql/"

def main():
    # Setup GraphQL client
    transport = RequestsHTTPTransport(
        url=GRAPHQL_ENDPOINT,
        use_json=True,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # GraphQL query: fetch recent orders (example query)
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
        with open("/tmp/orderreminderslog.txt", "a") as log:
            log.write(f"{datetime.now()}: Successfully fetched orders\n")
            for order in result.get("allOrders", []):
                log.write(f"Reminder sent to {order['customer']['email']} for order {order['id']}\n")
    except Exception as e:
        with open("/tmp/orderreminderslog.txt", "a") as log:
            log.write(f"{datetime.now()}: Error fetching orders - {str(e)}\n")

if __name__ == "__main__":
    main()
