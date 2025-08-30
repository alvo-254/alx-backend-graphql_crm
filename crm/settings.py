INSTALLED_APPS = [
    ...
    "django_crontab",
]
CRONJOBS = [
    ("*/5 * * * *", "crm.cron.log_crm_heartbeat"),  # runs every 5 minutes
]
