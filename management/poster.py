
import logging
import requests

from django.conf import settings
from abc import ABCMeta, abstractmethod

audit_logger = logging.getLogger('audit')


class ProductPoster(metaclass=ABCMeta):

    @abstractmethod
    def post_product(self, product):
        """
        Post the product to other website.
        :return: status code
        """
        return None


class EventbritePoster(ProductPoster):

    def post_product(self, product):
        url = "https://www.eventbriteapi.com/v3/events/"
        header = {
            "Authorization": "Bearer " + settings.EVENTBRITE_TOKEN,
        }
        payload = {
            "event.name.html": product.name,
            "event.start.utc": '2018-02-9T13:00:00Z',
            # "event.start.utc": product.start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.start.timezone": "UTC",
            "event.end.utc": '2018-02-10T13:00:00Z',
            # "event.end.utc": product.end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.end.timezone": "UTC",
            "event.currency": "USD"
        }
        response = requests.post(url=url, headers=header, data=payload, verify=True)
        print(response.json())
        print(response.status_code)
        if response.status_code != 200:
            audit_logger.info(str(response.json()))

        return response.status_code


