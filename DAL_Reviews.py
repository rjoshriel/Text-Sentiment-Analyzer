# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:22:23 2019

@author: josh
"""

import sqlite3
class DAL_rev(object):
    
    def sorting(self):
        conn = sqlite3.connect('products.db')
        que = "SELECT * FROM Reviews ORDER BY rating desc"
        res = conn.execute(que)
        return res
        
    def goodReview(self):
        conn = sqlite3.connect('products.db')
        que = "SELECT * FROM Reviews WHERE rating >= 3 ORDER BY rating desc"
        res = conn.execute(que)
        return res
    
    def badReview(self):
        conn = sqlite3.connect('products.db')
        que = "SELECT * FROM Reviews WHERE rating < 3 ORDER BY rating desc"
        res = conn.execute(que)
        return res