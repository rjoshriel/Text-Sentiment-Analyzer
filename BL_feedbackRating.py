# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:36:09 2019

@author: ELVIN
"""

from DAL_feedbackRating import DAL_feedRate

class BL_feedRate(object):
    
    def addFeed (self, ra, re):
        add = DAL_feedRate()
        fr = add.addFeed(ra, re)
        return fr