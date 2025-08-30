import datetime
import logging
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    """Logs a heartbeat entry and optionally checks GraphQL hello query"""
    log_file = "/tmp/crm_heartbeat_log.txt"  # <-- fixed file name
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Optional: verify GraphQL hello endpoint
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql/",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("{ hello }")
        result = client.execute(query)
        heartbeat_message = f"[{now}] Heartbeat OK | GraphQL says: {result.get('hello')}\n"
    except Exception as e:
        heartbeat_message = f"[{now}] Heartbeat ERROR: {str(e)}\n"

    with open(log_file, "a") as f:
        f.write(heartbeat_message)
