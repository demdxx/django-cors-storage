# -*- coding: utf-8 -*-

from django.conf import settings

from .base import Record

def get_bakend():
    return __import__( getattr(settings,'CORS_CACHE_BACKEND','corstorage.backend.dummy.Dummy') )

class Tracker:
    def __init__(self):
        self.__dict = {}
        self._backend = get_bakend()
    
    def __getitem__(self,key):
        if self.__dict.has_key(key):
            return self.__dict[key]
        return self.__dict[key] = Record(self._backend.get(key))

    def save(self):
        for key, record in self.__dict.iteritems():
            if record and record.is_modified():
                data = record.get_data()
                if not data:
                    self._backend.delete(key)
                else:
                    self._backend.set(key,data)

tracker = Tracker()

