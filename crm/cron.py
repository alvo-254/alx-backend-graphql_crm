#!/usr/bin/env python3
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    """
    Logs a heartbeat message with timestamp and optionally queries GraphQL hello field.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Default message
    message = f"[{now}] CRM Heartbeat OK"

    try:
        # Setup GraphQL client
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql/",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Run hello query
        query = gql("""
        query {
          hello
        }
        """)
        result = client.execute(query)
        hello_msg = result.get("hello", "No response")
        message += f" | GraphQL says: {hello_msg}"
    except Exception as e:
        message += f" | GraphQL query failed: {str(e)}"

    # Write to log
    with open("/tmp/crmheartbeatlog.txt", "a") as log:
        log.write(message + "\n")
