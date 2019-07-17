# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_ViewRecords.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
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
        self.load.setGeometry(QtCore.QRect(370, 340, 81, 31))
        self.load.setObjectName("load")
        self.back = QtWidgets.QPushButton(viewRecords)
        self.back.setGeometry(QtCore.QRect(370, 380, 81, 31))
        self.back.setObjectName("back")

        self.retranslateUi(viewRecords)
        QtCore.QMetaObject.connectSlotsByName(viewRecords)

    def retranslateUi(self, viewRecords):
        _translate = QtCore.QCoreApplication.translate
        viewRecords.setWindowTitle(_translate("viewRecords", "View Records"))
        self.load.setText(_translate("viewRecords", "Load"))
        self.back.setText(_translate("viewRecords", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewRecords = QtWidgets.QDialog()
    ui = Ui_viewRecords()
    ui.setupUi(viewRecords)
    viewRecords.show()
    sys.exit(app.exec_())

