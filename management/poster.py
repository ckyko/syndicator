
import logging
import requests

from django.conf import settings
from abc import ABCMeta, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


class TicketbudPoster(ProductPoster):

    def post_product(self, product):
        url = "https://ticketbud.com/users/sign_in"

        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element_by_id("user_email").send_keys("ckykokoko@gmail.com")
        driver.find_element_by_id("user_password").send_keys(settings.TICKETBUD_PASSWORD)
        driver.find_element_by_id("user_password").send_keys(Keys.RETURN)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Start New Event"))
        )
        element.send_keys(Keys.RETURN)
        driver.find_element_by_id("event-title").send_keys("title_for_test")
        start_time_elem = driver.find_element_by_id("event-start")
        start_time_elem.clear()
        start_time_elem.send_keys("2/22/2018")
        end_time_elem = driver.find_element_by_id("event-end")
        end_time_elem.clear()
        end_time_elem.send_keys("2/28/2018")
        driver.find_element_by_xpath("//*[@id='start-your-event-step-three']/div/ul/li[2]/a").send_keys(Keys.RETURN)
        driver.find_element_by_xpath("//*[@id='start-your-event-continue-controls']/button").send_keys(Keys.RETURN)
        driver.close()

        return 200


class TicketleapPoster(ProductPoster):

    def post_product(self, product):
        url = "https://www.ticketleap.com/login/"

        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element_by_name("username").send_keys("ckykokoko@gmail.com")
        driver.find_element_by_name("password").send_keys(settings.TICKETLEAP_PASSWORD)
        driver.find_element_by_id("email_login_button").send_keys(Keys.RETURN)
        driver.find_element_by_id("seller-nav-manage-events").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("a.create-event-button").send_keys(Keys.RETURN)
        driver.find_element_by_id("id_title").send_keys("e1")
        elem = driver.find_element_by_id("id_slug").send_keys("e1")
        # elem.send_keys(Keys.TAB + "aaaaaaaaaaaa")
        # driver.find_element_by_css_selector("body.cke_editable_themed").send_keys("e111")
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe.cke_wysiwyg_frame"))
        des = driver.find_element_by_tag_name("p")
        # des = driver.find_element_by_xpath("/html/body/p")
        # driver.execute_script("arguments[0].textContent = arguments[1];", des, "test description")

        # elem.clear()
        # elem.send_keys(Keys.RETURN)
        # driver.close()

        return 400


class TicketmasterPoster(ProductPoster):
    """
    see https://developer.ticketmaster.com/products-and-docs/apis/publish/#overview
    """

    def post_product(self, product):
        url = "https://app.ticketmaster.com/publish/v2/events?apikey=" + ""
        payload = {
            "source": {
                "id": "test_id_0009",
                "name": "test-source"
            },
            "test": True,
            "names": {
                "en-us": "example test event tnt1"
            },
            "publicVisibility": {
                "startDateTime": "2015-10-29T15:00:00Z",
                "visible": True
            },
            "dates": {
                "start": {
                    "dateTime": "2016-04-15T01:00:00Z",
                    "localDate": "2016-04-14",
                    "localTime": "19:00:00"
                },
                "timezone": "America/Edmonton"
            },
            "venue": {
                "source": {
                    "id": "test_venue_id_0001",
                    "name": "test-source"
                }
            }
        }
        response = requests.post(url=url, data=payload, verify=True)
        print(response.status_code)

        return response.status_code


