INSTALLED_APPS = [
    # ...
    "django_celery_beat",
    "django_crontab",
]

CRONJOBS = [
    ("*/5 * * * *", "crm.cron.log_crm_heartbeat"),  # runs every 5 minutes
]

# Celery configuration
CELERY_BROKER_URL = "redis://localhost:6379/0"  # adjust if using RabbitMQ
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "generate-crm-report-every-day": {
        "task": "crm.tasks.generatecrmreport",
        "schedule": crontab(hour=0, minute=0),  # runs daily at midnight
    },
}
