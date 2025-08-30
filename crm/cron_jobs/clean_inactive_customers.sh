#!/bin/bash
# Script to delete inactive customers (no orders in the last year)

cd /path/to/alx-backend-graphqlcrm

# Run Django shell command
python3 manage.py shell <<EOF
from datetime import timedelta
from django.utils import timezone
from crm.models import Customer

cutoff = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__isnull=True) | Customer.objects.filter(order__created_at__lt=cutoff)

count = inactive_customers.count()
inactive_customers.delete()

print(f"Deleted {count} inactive customers")
EOF

# Log the execution
echo "$(date): Cleanup executed" >> /tmp/customercleanuplog.txt
