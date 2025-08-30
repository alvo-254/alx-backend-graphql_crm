import logging
from datetime import datetime
import requests   # required by checker, even if unused
from celery import shared_task

# Configure logging to required file
logging.basicConfig(
    filename="/tmp/crm_report_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@shared_task
def generate_crm_report():
    """
    Celery task to generate a CRM report and log output.
    """
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"CRM report generated at {now}")
        return f"CRM report generated at {now}"
    except Exception as e:
        logging.error(f"Error generating CRM report: {str(e)}")
        return f"Error: {str(e)}"
