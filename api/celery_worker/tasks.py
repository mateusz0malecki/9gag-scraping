import logging

from celery import Task

from .celery import app
from db.database import db_session
from notifications.notification_email import send_email_notification
from notifications.notification_slack import send_slack_notification
from scraping.scraping_9gag import get_9gag_memes_info

logging.getLogger(__name__)


class SQLAlchemyTask(Task):
    """
    An abstract Celery Task that ensures that the connection the
    database is closed on task completion
    """
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db_session.remove()


@app.task(name="scraping", base=SQLAlchemyTask)
def scraping():
    try:
        get_9gag_memes_info(db_session)
    except Exception as e:
        logging.error(e)
        send_email_notification(f"""
        Your scraping functions failed to succeed their job.
        
        Details: {e}
        
        For more info please visit logs files."""
                                )
        send_slack_notification(f":rotating_light: *SCRAPING FAIL* \n:scroll: Details: {e} "
                                f"\n:information_source: For more info please visit logs files.")
