# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:23:57 2021

@author: belen
"""

class Teacher:
    def __init__(self, first, last, availability):
        self.first = first
        self.last = last
        self.availability = availability
        self.full_name = self.first + ' ' + self.last
        
    def __str__(self):
        return f'''
    Full Name: {self.full_name}
    Availability: {self.availability}
    '''