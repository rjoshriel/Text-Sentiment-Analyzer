# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:23:47 2019

@author: josh
"""

from DAL_Reviews import DAL_rev

class BL_Reviews(object):
    
    def sorting(self):
        DA_sort = DAL_rev()
        user=DA_sort.sorting()
        return user

    def goodReview(self):
        DA_goodRev = DAL_rev()
        user=DA_goodRev.goodReview()
        return user     
    
    def badReview(self):
        DA_badRev = DAL_rev()
        user = DA_badRev.badReview()
        return user