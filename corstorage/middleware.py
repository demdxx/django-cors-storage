# -*- coding: utf-8 -*-
from django.conf import settings

from .tracker import tracker

class CorStorageMiddleware(object):
    def process_request(self, request):
        tracker.clear()

    def process_response(self, request, response):
        tracker.save()
        return response