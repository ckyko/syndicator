import logging
from django_cron import CronJobBase, Schedule
from .models import Product, ProductType
audit_logger = logging.getLogger('audit')


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'management.test'    # a unique code

    def do(self):
        audit_logger.info('get in to cron job.....')
        products = Product.objects.all()
        print("in my cron job....... success")
        audit_logger.info('get in to cron job end.....')
