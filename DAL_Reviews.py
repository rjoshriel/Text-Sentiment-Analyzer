# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:17:51 2019

@author: ELVIN
"""

import sqlite3

class DAL_rev(object):
    
    def sorting(self,user):
        conn = sqlite3.connect('products.db')
        que = "SELECT * FROM Reviews ORDER BY rating desc"
        res = conn.execute(que)
        self.tableWidget.setRowCount(0)
        return res
        
    def goodReview(self,user):
        conn = sqlite3.connect('products.db')
        que = "SELECT * FROM Reviews WHERE rating >= 3 ORDER BY rating desc"
        res = conn.execute(que)
        self.tableWidget.setRowCount(0)
        return res
        
    def badReview(self,user):
        conn = sqlite3.connect('products.db')
        que = "SELECT * FROM Reviews WHERE rating < 3 ORDER BY rating desc"
        res = conn.execute(que)
        self.tableWidget.setRowCount(0) 
        return res