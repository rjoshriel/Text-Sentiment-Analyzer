from PyQt5 import QtCore, QtGui, QtWidgets
from BL_rev import BL_Reviews
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
        self.load.clicked.connect(self.sorting)
        self.pushButton.clicked.connect(self.goodReview)
        self.pushButton_2.clicked.connect(self.badReview)
    def retranslateUi(self, viewRecords):
        _translate = QtCore.QCoreApplication.translate
        viewRecords.setWindowTitle(_translate("viewRecords", "View Records"))
        self.load.setText(_translate("viewRecords", "Load"))
        self.back.setText(_translate("viewRecords", "Exit"))
        self.pushButton.setText(_translate("viewRecords", "Good"))
        self.pushButton_2.setText(_translate("viewRecords", "Bad"))
        self.label.setText(_translate("viewRecords", "<html><head/><body><p><span style=\" font-weight:600;\">REVIEWS</span></p></body></html>"))
        
    def sorting(self):
        sort=BL_Reviews()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(sort.sorting()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
    def goodReview(self):
        good=BL_Reviews()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(good.goodReview()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
    def badReview(self):
        bad=BL_Reviews()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(bad.badReview()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewRecords = QtWidgets.QDialog()
    ui = Ui_viewRecords()
    ui.setupUi(viewRecords)
    viewRecords.show()
    sys.exit(app.exec_())