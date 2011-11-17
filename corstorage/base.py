# -*- coding: utf-8 -*-

class Record(object):
    """
    Item record
    """
    def __init__(self,key,value):
        self.__dict = dict(value) if value else {}
        self._key = key
        self._modified = False
    
    def __eq__(self,key):
        return self._key == key
    
    def __setitem__(self, key, value):
        self.__dict[key] = value
        self._modified = True

    def __getitem__(self,key):
        return self.__dict[key] if key in self.__dict else None

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
        """
        Get value and remove key
        """
        return self.pop(key,value)
