import os

from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from puncher import punch


PUNCH_MINUTE = os.environ.get('PUNCH_MINUTE', '0')
PUNCH_HOUR = os.environ.get('PUNCH_HOUR', '9,19')
PUNCH_DAY_OF_WEEK = os.environ.get('PUNCH_DAY_OF_WEEK', 'mon,tue,wed,thu,fri')
TIMEZONE = os.environ.get('TIMEZONE', 'Asia/Taipei')

ACUD = os.environ.get('ACUD')
ACCOUNT = os.environ.get('ACCOUNT')
PASSWORD = os.environ.get('PASSWORD')
WAIT_SECONDS = 10

celery = Celery(__name__)
celery.conf.timezone = TIMEZONE
celery.conf.broker_url = os.environ.get(
    'CELERY_BROKER_URL',
    'redis://redis:6379/1',
)
logger = get_task_logger(__name__)


@celery.task
def auto_punch_in_and_out():
    punch(
        acud_token=ACUD,
        account=ACCOUNT,
        password=PASSWORD,
        wait_second=WAIT_SECONDS,
    )


celery.conf.beat_schedule = {
    'punch-task': {
        'task': 'main.auto_punch_in_and_out',
        'schedule': crontab(
            minute=PUNCH_MINUTE,
            hour=PUNCH_HOUR,
            day_of_week=PUNCH_DAY_OF_WEEK,
        ),
    }
}