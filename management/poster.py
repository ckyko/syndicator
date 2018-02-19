
import logging
import requests

from django.conf import settings
from abc import ABCMeta, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

audit_logger = logging.getLogger('audit')
DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'


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
            "event.start.utc": '2018-05-9T13:00:00Z',
            # "event.start.utc": product.start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.start.timezone": "UTC",
            "event.end.utc": '2018-05-10T13:00:00Z',
            # "event.end.utc": product.end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "event.end.timezone": "UTC",
            "event.currency": "USD"
        }
        response = requests.post(url=url, headers=header, data=payload, verify=True)
        if response.status_code != 200:
            audit_logger.info(str(response.json()))

        return response.status_code


class EventfulPoster(ProductPoster):

    def post_product(self, product):
        url = "http://eventful.com/events/new"
        # api = API('zzcNZHkCFvdT75KC')

        # If you need to log in:
        # api.login('ckykokoko2848f', '321321')
        #
        # events = api.call('/events/search', q='music', l='San Diego')
        # for event in events['events']['event']:
        #     print("%s at %s" % (event['title'], event['venue_name']))

        return 200


class TicketbudPoster(ProductPoster):

    def post_product(self, product):
        url = "https://ticketbud.com/users/sign_in"

        # driver = webdriver.Chrome()
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = DEFAULT_USER_AGENT
        driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'], desired_capabilities=dcap)
        driver.implicitly_wait(10)
        driver.get(url)
        driver.find_element_by_id("user_email").send_keys("ckykokoko@gmail.com")
        driver.find_element_by_id("user_password").send_keys(settings.TICKETBUD_PASSWORD)
        driver.find_element_by_id("user_password").send_keys(Keys.RETURN)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Start New Event"))
        )
        element.click()
        # title_element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "event-title"))
        # )
        # title_element.send_keys(product.name)
        driver.find_element_by_id("event-title").send_keys(product.name)
        start_time_elem = driver.find_element_by_id("event-start")
        start_time_elem.clear()
        start_time_elem.send_keys("2/22/2018")
        end_time_elem = driver.find_element_by_id("event-end")
        end_time_elem.clear()
        end_time_elem.send_keys("2/28/2018")
        driver.find_element_by_xpath("//*[@id='start-your-event-step-three']/div/ul/li[2]/a").send_keys(Keys.RETURN)
        driver.find_element_by_xpath("//*[@id='start-your-event-continue-controls']/button").click()
        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "copy-event-url-dashboard"))
        #     # EC.presence_of_element_located((By.XPATH, "//*[@id='admin-navigation-dashboard']/a"))
        # )
        copy_element = driver.find_element_by_id("copy-event-url-dashboard")
        copy_element.click()
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
        driver.find_element_by_id("id_slug").send_keys("e1")
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe.cke_wysiwyg_frame"))
        a = driver.page_source
        driver.find_element_by_xpath("/html/body").click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/p"))
        )
        driver.execute_script("arguments[0].textContent = arguments[1];", element, "test description")
        driver.switch_to.default_content()

        driver.find_element_by_xpath("//*[@id='create-event-appearance']/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='hero-image-dialog']/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]").click()
        driver.find_element_by_xpath("//*[@id='hero-image-dialog']/div[2]/div/div[2]/button[1]").click()

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


