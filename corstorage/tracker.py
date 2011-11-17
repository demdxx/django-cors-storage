# -*- coding: utf-8 -*-

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

from django.conf import settings
from django.utils import importlib

from .base import Record

def get_bakend():
    return importlib.import_module( getattr(settings,'CORS_STORAGE_BACKEND','corstorage.backend.dummy') ).Backend()

class Tracker:
    def __init__(self):
        _thread_locals.records = {}
        self._backend = get_bakend()
    
    def __getitem__(self,key):
        if _thread_locals.records.has_key(key):
            return _thread_locals.records[key]
        _thread_locals.records[key] = Record(key,self._backend.get(key))
        return _thread_locals.records[key]

    def reload(self,key):
        _thread_locals.records[key] = Record(key,self._backend.get(key))
        return _thread_locals.records[key]

    def clear(self):
        _thread_locals.records = {}

    def save(self):
        if _thread_locals.records:
            for key, record in _thread_locals.records.iteritems():
                if record and record.is_modified():
                    data = record.get_data()
                    if not data:
                        self._backend.delete(key)
                    else:
                        self._backend.set(key,data)

_thread_locals = local()
tracker = Tracker()

