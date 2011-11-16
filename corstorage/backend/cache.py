# -*- coding: utf-8 -*-

from django.core.cache import get_cache
from django.utils import simplejson
from django.conf import settings

CORS_STORAGE_CACHE = getattr(settings,'CORS_STORAGE_CACHE','default')

class Cache(object):
    def __init__(self):
        self._cache = get_cache( CORS_STORAGE_CACHE )
    
    def get(self,key):
        try:
            return simplejson.loads(self._cache.get(key))
        except (ValueError, TypeError):
            pass
        return None
    
    def set(self,key,value):
        self._cache.set(key,simplejson.dumps(value))

    def delete(self,key):
        self._cache.delete(key)
