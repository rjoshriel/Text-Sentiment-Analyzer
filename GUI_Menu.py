# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GUI_FeedbackRating import Ui_feedbackRating
from GUI_ViewRecords import Ui_viewRecords

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(255, 300)
        self.feedRate = QtWidgets.QPushButton(Menu)
        self.feedRate.setGeometry(QtCore.QRect(20, 40, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.feedRate.setFont(font)
        self.feedRate.setObjectName("feedRate")
        self.exitButton = QtWidgets.QPushButton(Menu)
        self.exitButton.setGeometry(QtCore.QRect(20, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.viewRec = QtWidgets.QPushButton(Menu)
        self.viewRec.setGeometry(QtCore.QRect(20, 120, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewRec.setFont(font)
        self.viewRec.setObjectName("viewRec")

        #Feedback Rating declaration
        self.feedbackRating = QtWidgets.QDialog()
        self.fbr = Ui_feedbackRating()
        self.fbr.setupUi(self.feedbackRating)
        
        #View Records declaration
        self.viewRecords = QtWidgets.QDialog()
        self.vr = Ui_viewRecords()
        self.vr.setupUi(self.viewRecords)

        #Button Signals
        self.exitButton.clicked.connect(self.exitButton_clicked)
        self.feedRate.clicked.connect(self.feedRate_clicked)
        self.feedRate.clicked.connect(self.feedRate_clicked)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.feedRate.setText(_translate("Menu", "Give Feedback and Rating"))
        self.exitButton.setText(_translate("Menu", "Exit"))
        self.viewRec.setText(_translate("Menu", "View Records"))
        
    #Feedback Button Definition
    def feedRate_clicked(self):      
        self.feedbackRating = QtWidgets.QDialog()
        self.fbr = Ui_feedbackRating()
        self.fbr.setupUi(self.feedbackRating)
        self.feedbackRating.show()
        Menu.close()
        
    #View Rec Button    
    def viewRec_clicked(self):
        self.viewRecords = QtWidgets.QDialog()
        self.vr = Ui_viewRecords()
        self.vr.setupUi(self.viewRecords)
        self.viewRecords.show()
        Menu.close()
    
    #Exit Button Definition    
    def exitButton_clicked(self):
        Menu.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

