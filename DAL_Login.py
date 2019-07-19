# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:02:03 2019

@author: ELVIN
"""

import sqlite3

class DAL_login(object):
    
    def add_User(self,user):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        sql = """INSERT INTO Reviews (Name) VALUES ('%s')""" %user
        cursor.execute(sql)
        conn.commit() 
        conn.close()
        
    def check_User(self,user):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM Reviews")
        rows = cursor.fetchone()