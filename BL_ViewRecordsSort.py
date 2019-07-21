# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:39:34 2019

@author: KEN
"""
from PyQt5 import QtWidgets
from DAL_ViewRecords import DAL_viewrecords
class BLviewrecords(object):
    def loaddata(self):
        con=DAL_viewrecords()
        for row_number, row_data in enumerate(con.loadData()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def Sorting(self):
        con=DAL_viewrecords()
        for row_number, row_data in enumerate(con.sorting()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
 