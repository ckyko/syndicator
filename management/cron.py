import logging
from datetime import datetime, timedelta

from django_cron import CronJobBase, Schedule

from .models import Product, ProductType
from .poster import EventbritePoster, TicketbudPoster

audit_logger = logging.getLogger('audit')


POSTERMAP = {
    'EventbritePoster': EventbritePoster,
    'TicketbudPoster': TicketbudPoster,
}


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'management.test'    # a unique code

    def do(self):
        audit_logger.info('---------------START CRON JOB-----------------')
        print('---------------START CRON JOB-----------------')
        products = Product.objects.filter(active=True, need_repost__isnull=False).distinct()
        print(products)

        # eventbrite_poster = EventbritePoster()
        # ticketbud_poster = TicketbudPoster()

        for product in products:
            for poster in product.need_repost.all():

                status = POSTERMAP[poster.name]().post_product(product)
                # status = eventbrite_poster.post_product(product)
                audit_logger.info(str(product) + ' - ' + str(status))
                if status == 200:
                    product.need_repost.remove(poster)
                    print("removed...")
                    # print(product.need_repost.all())
        audit_logger.info('---------------END CRON JOB---------------')




