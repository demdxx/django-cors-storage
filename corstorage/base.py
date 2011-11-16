# -*- coding: utf-8 -*-

class Record(object):
    """
    Item record
    """
    def __init__(self):
        self.__dict = {}
        self._modified = False
    
    def __setitem__(self, key, value):
        self.__dict[key] = value
        self._modified = True

    def __getitem__(self,key):
        return self.__dict.get(key)

    def modified(self,m):
        self._modified = m
    
    def is_modified(self):
        return self._modified

    def get_data(self):
        return self.__dict

    def inc(self,key):
        if self.__dict.has_key(key):
            self.__dict[key] += 1
        else:
            self.__dict[key] = 1
        return self

    def dec(self,key):
        if self.__dict.has_key(key):
            self.__dict[key] -= 1
        else:
            self.__dict[key] = -1
        return self

    def pop(self,key,value=None):
        return self.pop(key,value)
