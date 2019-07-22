# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctorLogin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from doctorPage import doctor_page
from doctorSignup import Ui_doctorSignupDialog


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

class Ui_doctorDialog(object):
    def showAlert(self,title,message):
        msgBox = QtGui.QMessageBox()
        #msgBox.setIcon(msgBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(msgBox.Ok)
        msgBox.exec_()
    def signinWindow(self):
        self.signinwindow = QtGui.QDialog()
        self.ui = doctor_page()
        self.ui.setupUi(self.signinwindow)
        self.signinwindow.show()

    def logincheck(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()

        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        result = c.execute('SELECT * FROM Doctor WHERE Username = ? AND Password = ?',(username,password))
        conn.commit()
        if len(result.fetchall()) > 0:
            self.signinWindow()
        else:
            self.showAlert('Warning','   Invalid Doctor !')
    def signupEvent(self):
        self.signupwindow = QtGui.QDialog()
        self.ui = Ui_doctorSignupDialog()
        self.ui.setupUi(self.signupwindow)
        self.signupwindow.show()

    def setupUi(self, doctorDialog):
        doctorDialog.setObjectName(_fromUtf8("doctorDialog"))
        doctorDialog.resize(478, 481)
        doctorDialog.setStyleSheet(_fromUtf8("QDialog{\n"
        "    \n"
        "    background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 rgba(41, 156, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "}"))
        self.label = QtGui.QLabel(doctorDialog)
        self.label.setGeometry(QtCore.QRect(150, 80, 211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.usernameLabel = QtGui.QLabel(doctorDialog)
        self.usernameLabel.setGeometry(QtCore.QRect(100, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))

        self.passwordLabel = QtGui.QLabel(doctorDialog)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 200, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))

        self.usernameEdit = QtGui.QLineEdit(doctorDialog)
        self.usernameEdit.setGeometry(QtCore.QRect(190, 170, 113, 20))
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))

        self.passwordEdit = QtGui.QLineEdit(doctorDialog)
        self.passwordEdit.setGeometry(QtCore.QRect(190, 200, 113, 20))
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.passwordEdit.setEchoMode(self.passwordEdit.Password)

        self.loginBtn = QtGui.QPushButton(doctorDialog)
        self.loginBtn.setGeometry(QtCore.QRect(190, 250, 81, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.loginBtn.clicked.connect(self.logincheck)

        self.signupBtn = QtGui.QPushButton(doctorDialog)
        self.signupBtn.setGeometry(QtCore.QRect(280, 250, 81, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.signupBtn.setFont(font)
        self.signupBtn.setObjectName(_fromUtf8("signupBtn"))
        self.signupBtn.clicked.connect(self.signupEvent)

        self.retranslateUi(doctorDialog)
        QtCore.QMetaObject.connectSlotsByName(doctorDialog)

    def retranslateUi(self, doctorDialog):
        doctorDialog.setWindowTitle(_translate("doctorDialog", "Doctor Login", None))
        self.label.setText(_translate("doctorDialog", "Doctor Login", None))
        self.usernameLabel.setText(_translate("doctorDialog", "Username", None))
        self.passwordLabel.setText(_translate("doctorDialog", "Password", None))
        self.loginBtn.setText(_translate("doctorDialog", "Login", None))
        self.signupBtn.setText(_translate("doctorDialog", "Sign up", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    doctorDialog = QtGui.QDialog()
    ui = Ui_doctorDialog()
    ui.setupUi(doctorDialog)
    doctorDialog.show()
    sys.exit(app.exec_())
