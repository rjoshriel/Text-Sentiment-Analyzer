# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:48:11 2019

@author: ELVIN
"""

from DAL_Reviews import DAL_rev

class BL_Reviews(object):
    
    def sorting(self, uLine):
        DA_sort = DAL_rev()
        user = DA_sort.sorting(uLine)
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def goodReview(self, uLine):
        DA_goodRev = DAL_rev()
        user = DA_goodRev.goodReview(uLine)
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
    def badReview(self, uLine):
        DA_badRev = DAL_rev()
        user = DA_badRev.badReview(uLine)
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))