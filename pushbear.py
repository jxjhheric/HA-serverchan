"""
Weixin Push Service by pushbear
"""
import logging
from fake_useragent import UserAgent
import datetime
import requests
import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_MESSAGE, ATTR_TITLE, ATTR_DATA, ATTR_TARGET, PLATFORM_SCHEMA, BaseNotificationService)
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)
_RESOURCE = 'https://pushbear.ftqq.com'

CONF_SENDKEY = 'sendkey'

def get_service(hass, config, discovery_info=None):
    """Get the ServerChan notification service."""
    sendkey = config.get(CONF_SENDKEY)
    return ServerchanNotificationService(hass, sendkey)


class ServerchanNotificationService(BaseNotificationService):
    """Implementation of the notification service for SimplePush."""

    def __init__(self, hass, sendkey):
        """Initialize the service."""
        _LOGGER.debug("INIT message")
        self._sendkey = sendkey

    def send_message(self, message='', **kwargs):
        """Send a message to a user."""
        url = '{}/sub?sendkey={}&'.format(_RESOURCE, self._sendkey)
        title = kwargs.get(ATTR_TITLE)
        if title:
           timestp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           sendmessage = '{} \n{}'.format(message, timestp)
           payload = {'text': title, 'desp': sendmessage}
           ua = UserAgent()
           header = {'user-agent': ua.random }
           response = requests.get(url,params = payload,headers = header)
           _LOGGER.debug("sneding out message")
		
           if response.status_code != 200:
              obj = response.json()
              error_message = obj['error']['message']
              error_code = obj['error']['code']
              _LOGGER.error(
                   "Error %s : %s (Code %s)", resp.status_code, error_message,
                   error_code)
        else:
           _LOGGER.error("Title can NOT be null")
