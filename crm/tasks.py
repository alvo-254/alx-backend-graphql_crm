import logging
from datetime import datetime
from celery import shared_task

# Configure logging to required file
logging.basicConfig(
    filename="/tmp/crmreportlog.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@shared_task
def generatecrmreport():
    """
    Celery task to generate a CRM report.
    """
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"CRM report generated at {now}")
        return f"CRM report generated at {now}"
    except Exception as e:
        logging.error(f"Error generating CRM report: {str(e)}")
        return f"Error: {str(e)}"
