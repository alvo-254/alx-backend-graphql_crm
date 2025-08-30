import datetime
import requests
from celery import shared_task

@shared_task
def generate_crm_report():
    url = "http://localhost:8000/graphql"
    query = """
    query {
      totalCustomers
      totalOrders
      totalRevenue
    }
    """
    response = requests.post(url, json={'query': query})
    data = response.json().get("data", {})

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{ts} - Report: {data.get('totalCustomers')} customers, {data.get('totalOrders')} orders, {data.get('totalRevenue')} revenue\n"

    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(log_line)
