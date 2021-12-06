import logging

from rest_framework.views import APIView
from rest_framework.response import Response

class ShowMessage(APIView):
    def get(self, request, format=None):
        msg = {"message":"hello"}
        logger = logging.getLogger('watchtower-logger')
        logger.info("Testing Logs")
        logger.error('test1!')
        return Response(msg)