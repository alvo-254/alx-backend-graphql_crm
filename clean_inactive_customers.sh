#!/bin/bash
# Deletes inactive customers (no orders in a year)

timestamp=$(date '+%Y-%m-%d %H:%M:%S')
deleted=$(python manage.py shell -c "
from crm.models import Customer
from django.utils import timezone
from datetime import timedelta

cutoff = timezone.now() - timedelta(days=365)
qs = Customer.objects.filter(orders__isnull=True, created_at__lt=cutoff)
count = qs.count()
qs.delete()
print(count)
")

echo "$timestamp - Deleted $deleted inactive customers" >> /tmp/customer_cleanup_log.txt
