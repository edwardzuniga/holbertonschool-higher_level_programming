#!/usr/bin/python3


'''Student to JSON with filter'''


class Student:
    '''Initialitation'''
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Public method'''

        n_dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                n_dic[i] = getattr(self, i)
        return n_dic
