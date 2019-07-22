# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctorSignup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3

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

class Ui_doctorSignupDialog(object):
    def showAlert(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(msgBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(msgBox.Ok)
        msgBox.exec_()

    def insertData(self):
        name = self.nameEdit.text()
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()
        email = self.emailEdit.text()
        phone = self.phoneEdit.text()

        conn = sqlite3.connect('login.db')
        if username == '' or password == '' or email == '' or name == '' or phone == '':
            self.showAlert('Warning','All fields are mandatory !')
        else:
            result = conn.execute("SELECT * FROM Doctor WHERE Username = ? AND Password = ?",(username,password))
            if len(result.fetchall())>0:
                self.showAlert('Warning','  User Already Exists !!!  ')
            else:
                conn.execute("INSERT INTO Doctor VALUES(?,?,?,?,?)",(name,username,password,email,phone))
                # Create table of new user
                #conn.execute("CREATE TABLE IF NOT EXISTS "+username+"(datestamp TEXT, emg REAL, temp REAL)")

                self.showAlert('Congratulations !!','  Account created !!  ')
                conn.commit()
                conn.close()

    def setupUi(self, doctorSignupDialog):
        doctorSignupDialog.setObjectName(_fromUtf8("doctorSignupDialog"))
        doctorSignupDialog.resize(478, 481)
        doctorSignupDialog.setStyleSheet(_fromUtf8("QDialog{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 rgba(41, 156, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.label = QtGui.QLabel(doctorSignupDialog)
        self.label.setGeometry(QtCore.QRect(150, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.nameLabel = QtGui.QLabel(doctorSignupDialog)
        self.nameLabel.setGeometry(QtCore.QRect(100, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))

        self.usernameLabel = QtGui.QLabel(doctorSignupDialog)
        self.usernameLabel.setGeometry(QtCore.QRect(100, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))

        self.passwordLabel = QtGui.QLabel(doctorSignupDialog)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 200, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))

        self.passwordLabel_2 = QtGui.QLabel(doctorSignupDialog)
        self.passwordLabel_2.setGeometry(QtCore.QRect(100, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.passwordLabel_2.setFont(font)
        self.passwordLabel_2.setObjectName(_fromUtf8("passwordLabel_2"))

        self.passwordLabel_3 = QtGui.QLabel(doctorSignupDialog)
        self.passwordLabel_3.setGeometry(QtCore.QRect(100, 260, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(11)
        self.passwordLabel_3.setFont(font)
        self.passwordLabel_3.setObjectName(_fromUtf8("passwordLabel_3"))

        self.nameEdit = QtGui.QLineEdit(doctorSignupDialog)
        self.nameEdit.setGeometry(QtCore.QRect(190, 140, 113, 20))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))

        self.usernameEdit = QtGui.QLineEdit(doctorSignupDialog)
        self.usernameEdit.setGeometry(QtCore.QRect(190, 170, 113, 20))
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))

        self.passwordEdit = QtGui.QLineEdit(doctorSignupDialog)
        self.passwordEdit.setGeometry(QtCore.QRect(190, 200, 113, 20))
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))

        self.emailEdit = QtGui.QLineEdit(doctorSignupDialog)
        self.emailEdit.setGeometry(QtCore.QRect(190, 230, 113, 20))
        self.emailEdit.setObjectName(_fromUtf8("emailEdit"))

        self.phoneEdit = QtGui.QLineEdit(doctorSignupDialog)
        self.phoneEdit.setGeometry(QtCore.QRect(190, 260, 113, 20))
        self.phoneEdit.setObjectName(_fromUtf8("phoneEdit"))

        self.signupBtn = QtGui.QPushButton(doctorSignupDialog)
        self.signupBtn.setGeometry(QtCore.QRect(190, 310, 111, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.signupBtn.setFont(font)
        self.signupBtn.setObjectName(_fromUtf8("signupBtn"))
        self.signupBtn.clicked.connect(self.insertData)

        self.retranslateUi(doctorSignupDialog)
        QtCore.QMetaObject.connectSlotsByName(doctorSignupDialog)

    def retranslateUi(self, doctorSignupDialog):
        doctorSignupDialog.setWindowTitle(_translate("doctorSignupDialog", "Create Account", None))
        self.label.setText(_translate("doctorSignupDialog", "Create Account", None))
        self.nameLabel.setText(_translate("doctorSignupDialog", "Name", None))
        self.usernameLabel.setText(_translate("doctorSignupDialog", "Username", None))
        self.passwordLabel.setText(_translate("doctorSignupDialog", "Password", None))
        self.signupBtn.setText(_translate("doctorSignupDialog", "Sign up", None))
        self.passwordLabel_2.setText(_translate("doctorSignupDialog", "Email", None))
        self.passwordLabel_3.setText(_translate("doctorSignupDialog", "Phone", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    doctorSignupDialog = QtGui.QDialog()
    ui = Ui_doctorSignupDialog()
    ui.setupUi(doctorSignupDialog)
    doctorSignupDialog.show()
    sys.exit(app.exec_())
