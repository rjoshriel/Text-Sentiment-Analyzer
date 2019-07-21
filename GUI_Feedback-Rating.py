# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_FeedRate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BL_feedbackRating import BL_feedRate
#from GUI_dataSorting import Ui_Dialog

class Ui_feedbackRating(object):
    def setupUi(self, feedbackRating):
        feedbackRating.setObjectName("feedbackRating")
        feedbackRating.resize(352, 232)
        self.feedback = QtWidgets.QLabel(feedbackRating)
        self.feedback.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.feedback.setFont(font)
        self.feedback.setObjectName("feedback")
        self.textEdit = QtWidgets.QTextEdit(feedbackRating)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 331, 131))
        self.textEdit.setObjectName("textEdit")
        self.rating = QtWidgets.QLabel(feedbackRating)
        self.rating.setGeometry(QtCore.QRect(10, 190, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rating.setFont(font)
        self.rating.setObjectName("rating")
        self.comboBox = QtWidgets.QComboBox(feedbackRating)
        self.comboBox.setGeometry(QtCore.QRect(70, 190, 61, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("0")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")
        self.comboBox.addItem("5")
        self.submitButton = QtWidgets.QPushButton(feedbackRating)
        self.submitButton.setGeometry(QtCore.QRect(260, 190, 75, 23))
        self.submitButton.setObjectName("submitButton")
        
        #Button Signal      
        self.submitButton.clicked.connect(self.submitButton_clicked)
        self.submitButton.clicked.connect(self.feedRate)

        self.retranslateUi(feedbackRating)
        QtCore.QMetaObject.connectSlotsByName(feedbackRating)

    def retranslateUi(self, feedbackRating):
        _translate = QtCore.QCoreApplication.translate
        feedbackRating.setWindowTitle(_translate("feedbackRating", "Dialog"))
        self.feedback.setText(_translate("feedbackRating", "Enter Feedback:"))
        self.rating.setText(_translate("feedbackRating", "Rating:"))
        self.submitButton.setText(_translate("feedbackRating", "Submit"))

    #Add Feedback and Rating
    def feedRate(self):
        feedRating = BL_feedRate()
        rev = self.textEdit.toPlainText()
        rate = self.comboBox.currentText()
        feedRating.addFeed(rate,rev)

    #Submit Button definition
    def submitButton_clicked(self):
        feedbackRating.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    feedbackRating = QtWidgets.QDialog()
    ui = Ui_feedbackRating()
    ui.setupUi(feedbackRating)
    feedbackRating.show()
    sys.exit(app.exec_())

