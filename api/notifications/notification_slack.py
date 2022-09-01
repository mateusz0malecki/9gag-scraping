import logging

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from settings import get_settings

app_settings = get_settings()
logger = logging.getLogger(__name__)


def send_slack_notification(message):
    client = WebClient(token=app_settings.slack_bot_oauth_token)
    try:
        client.chat_postMessage(
            channel=app_settings.slack_channel_id,
            text=message,
            mrkdwn=True
        )
    except SlackApiError as e:
        logging.error(e)
