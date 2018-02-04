import logging

from django_cron import CronJobBase, Schedule

from .models import Product, ProductType
from .poster import EventbritePoster

# audit_logger = logging.getLogger('audit')


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'management.test'    # a unique code

    def do(self):
        # audit_logger.info('---------------START CRON JOB-----------------')
        print('---------------START CRON JOB-----------------')
        products = Product.objects.filter(active=True, is_posted_to_other=False)

        eventbrite_poster = EventbritePoster()
        for product in products:
            status = eventbrite_poster.post_product(product)
            # audit_logger.info(str(product) + ' - ' + str(status))
            if status == 200:
                product.is_posted_to_other = True
                product.save()
        # audit_logger.info('---------------END CRON JOB---------------')




