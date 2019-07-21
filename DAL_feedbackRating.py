# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:41:17 2019

@author: ELVIN
"""

import sqlite3

class DAL_feedRate(object):
    
    def addFeed (self, rate, rev):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        user = cursor.execute('INSERT INTO Reviews (rating, review) VALUES (?, ?)', (int(rate), rev, ))
        conn.commit()