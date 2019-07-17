# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_FeedbackRating.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_feedbackRating(object):
    def setupUi(self, feedbackRating):
        feedbackRating.setObjectName("feedbackRating")
        feedbackRating.resize(400, 300)
        self.label = QtWidgets.QLabel(feedbackRating)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(feedbackRating)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 381, 161))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(feedbackRating)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setObjectName("label_2")
        self.submitButton = QtWidgets.QPushButton(feedbackRating)
        self.submitButton.setGeometry(QtCore.QRect(230, 260, 75, 23))
        self.submitButton.setObjectName("submitButton")
        self.cancelButton = QtWidgets.QPushButton(feedbackRating)
        self.cancelButton.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.comboBox = QtWidgets.QComboBox(feedbackRating)
        self.comboBox.setGeometry(QtCore.QRect(70, 220, 61, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["0", "1", "2", "3", "4", "5"])
        
        self.cancelButton.clicked.connect(self.cancelButton_clicked)

        self.retranslateUi(feedbackRating)
        QtCore.QMetaObject.connectSlotsByName(feedbackRating)


    def retranslateUi(self, feedbackRating):
        _translate = QtCore.QCoreApplication.translate
        feedbackRating.setWindowTitle(_translate("feedbackRating", "Feedback and Rating"))
        self.label.setText(_translate("feedbackRating", "Feedback:"))
        self.label_2.setText(_translate("feedbackRating", "Rating:"))
        self.submitButton.setText(_translate("feedbackRating", "Submit"))
        self.cancelButton.setText(_translate("feedbackRating", "Cancel"))
        
    def cancelButton_clicked(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    feedbackRating = QtWidgets.QDialog()
    ui = Ui_feedbackRating()
    ui.setupUi(feedbackRating)
    feedbackRating.show()
    sys.exit(app.exec_())

