from django.utils.deprecation import MiddlewareMixin

import logging

logger = logging.getLogger(__name__)


class Hello(MiddlewareMixin):
    def process_request(self, request):
        logger.debug('request in hello')

    def process_response(self, request, response):
        logger.debug('response from hello')
        return response
