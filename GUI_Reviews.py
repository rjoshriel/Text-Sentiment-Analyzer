# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_ViewRecords.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_viewRecords(object):
    def setupUi(self, viewRecords):
        viewRecords.setObjectName("viewRecords")
        viewRecords.resize(470, 417)
        self.tableWidget = QtWidgets.QTableWidget(viewRecords)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 341, 401))
        self.tableWidget.setRowCount(99)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.load = QtWidgets.QPushButton(viewRecords)
        self.load.setGeometry(QtCore.QRect(370, 330, 81, 31))
        self.load.setObjectName("load")
        self.back = QtWidgets.QPushButton(viewRecords)
        self.back.setGeometry(QtCore.QRect(370, 370, 81, 31))
        self.back.setObjectName("back")
        self.pushButton = QtWidgets.QPushButton(viewRecords)
        self.pushButton.setGeometry(QtCore.QRect(370, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(viewRecords)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(viewRecords)
        self.label.setGeometry(QtCore.QRect(380, 50, 51, 16))
        self.label.setObjectName("label")

        self.retranslateUi(viewRecords)
        QtCore.QMetaObject.connectSlotsByName(viewRecords)

    def retranslateUi(self, viewRecords):
        _translate = QtCore.QCoreApplication.translate
        viewRecords.setWindowTitle(_translate("viewRecords", "View Records"))
        self.load.setText(_translate("viewRecords", "Load"))
        self.back.setText(_translate("viewRecords", "Exit"))
        self.pushButton.setText(_translate("viewRecords", "Good"))
        self.pushButton_2.setText(_translate("viewRecords", "Bad"))
        self.label.setText(_translate("viewRecords", "<html><head/><body><p><span style=\" font-weight:600;\">REVIEWS</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewRecords = QtWidgets.QDialog()
    ui = Ui_viewRecords()
    ui.setupUi(viewRecords)
    viewRecords.show()
    sys.exit(app.exec_())

