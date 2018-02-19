import logging
from datetime import datetime, timedelta

from .models import Product, ProductType
from .poster import EventbritePoster, TicketbudPoster

audit_logger = logging.getLogger('audit')


POSTERMAP = {
    'EventbritePoster': EventbritePoster,
    'TicketbudPoster': TicketbudPoster,
}


class MyCronJob(object):
    def do(self):
        audit_logger.info('---------------START CRON JOB-----------------')
        products = Product.objects.filter(active=True, need_repost__isnull=False).distinct()

        for product in products:
            for poster in product.need_repost.all():

                status = POSTERMAP[poster.name]().post_product(product)
                audit_logger.info(str(product) + ' - ' + str(status))
                if status == 200:
                    product.need_repost.remove(poster)
        audit_logger.info('---------------END CRON JOB---------------')




