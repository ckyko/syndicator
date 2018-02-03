import logging
from django_cron import CronJobBase, Schedule
audit_logger = logging.getLogger('audit')


# def my_scheduled_job():
#     print('get in to cron job.....')
#     audit_logger.info('get in to cron job.....')

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'management.test'    # a unique code

    def do(self):
        print("in my cron job....... success")
