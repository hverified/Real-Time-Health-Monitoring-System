# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from login import login_Dialog
from doctorLogin import Ui_doctorDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def doctor(self):
        self.doctorwindow = QtGui.QDialog()
        self.ui = Ui_doctorDialog()
        self.ui.setupUi(self.doctorwindow)
        self.doctorwindow.show()

    def patient(self):
        self.patientwindow = QtGui.QDialog()
        self.ui = login_Dialog()
        self.ui.setupUi(self.patientwindow)
        self.patientwindow.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(480, 483)
        ###### Icon ############
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("apple.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        ########################

        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 rgba(41, 156, 255, 255), stop:1 rgba(255, 255, 255, 255));}"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        ###### Buttons #############
        self.doctorbtn = QtGui.QPushButton(Dialog)
        self.doctorbtn.setGeometry(QtCore.QRect(80, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.doctorbtn.setFont(font)
        self.doctorbtn.setObjectName(_fromUtf8("doctorbtn"))
        self.doctorbtn.clicked.connect(self.doctor)

        self.patientbtn = QtGui.QPushButton(Dialog)
        self.patientbtn.setGeometry(QtCore.QRect(80, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.patientbtn.setFont(font)
        self.patientbtn.setObjectName(_fromUtf8("patientbtn"))
        self.patientbtn.clicked.connect(self.patient)
        #################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Health Monitor", None))
        self.label.setText(_translate("Dialog", "Login as", None))
        self.doctorbtn.setText(_translate("Dialog", "Doctor", None))
        self.patientbtn.setText(_translate("Dialog", "Patient", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
