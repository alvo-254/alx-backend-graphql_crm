#!/bin/bash
# Script to delete inactive customers

timestamp=$(date +"%Y-%m-%d %H:%M:%S")
deleted=$(python manage.py shell -c "
from crm.models import Customer, Order
from datetime import timedelta, datetime
cutoff = datetime.now() - timedelta(days=365)
inactive = Customer.objects.exclude(order__order_date__gte=cutoff)
count = inactive.count()
inactive.delete()
print(count)
")
echo "$timestamp - Deleted $deleted inactive customers" >> /tmp/customer_cleanup_log.txt
