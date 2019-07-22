# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
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

class signup_Dialog(object):
    def showAlert(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(msgBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(msgBox.Ok)
        msgBox.exec_()

    def insertData(self):
        name = self.name_edit.text()
        username = self.username_edit.text()
        password = self.password_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        address = self.address_edit.text()

        conn = sqlite3.connect('login.db')
        if username == '' or password == '' or email == '' or name == '' or phone == '' or address == '':
            self.showAlert('Warning','All fields are mandatory !')
        else:
            result = conn.execute("SELECT * FROM login WHERE Username = ? AND Password = ?",(username,password))
            if len(result.fetchall())>0:
                self.showAlert('Warning','  User Already Exists !!!  ')
            else:
                conn.execute("INSERT INTO login VALUES(?,?,?,?,?,?)",(name,username,password,email,phone,address))
                # Create table of new user
                conn.execute("CREATE TABLE IF NOT EXISTS "+username+"(datestamp TEXT, emg REAL, temp REAL)")

                self.showAlert('Congratulations !!','  Account created !!  ')
                conn.commit()
                conn.close()



    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(478, 483)
        Dialog.setStyleSheet(_fromUtf8("QDialog{background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 rgba(41, 156, 255, 255), stop:1 rgba(255, 255, 255, 255));}"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 360, 131, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ############################################################
        self.pushButton.clicked.connect(self.insertData)
        ############################################################
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 400, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        ############################################################
        self.nameLabel = QtGui.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(90, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        ############################################################
        self.usernameLabel = QtGui.QLabel(Dialog)
        self.usernameLabel.setGeometry(QtCore.QRect(90, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        ############################################################
        self.passwordLabel = QtGui.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(90, 200, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        ############################################################
        self.emailLabel = QtGui.QLabel(Dialog)
        self.emailLabel.setGeometry(QtCore.QRect(90, 230, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName(_fromUtf8("label_4"))
        ############################################################
        self.phoneLabel = QtGui.QLabel(Dialog)
        self.phoneLabel.setGeometry(QtCore.QRect(90, 260, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.phoneLabel.setFont(font)
        self.phoneLabel.setObjectName(_fromUtf8("phoneLabel"))
        ############################################################
        self.addressLabel = QtGui.QLabel(Dialog)
        self.addressLabel.setGeometry(QtCore.QRect(90, 290, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        
        ######################## Line Edits ########################
        self.name_edit = QtGui.QLineEdit(Dialog)
        self.name_edit.setGeometry(QtCore.QRect(180, 140, 171, 20))
        self.name_edit.setObjectName(_fromUtf8("name_edit"))
        ############################################################
        self.username_edit = QtGui.QLineEdit(Dialog)
        self.username_edit.setGeometry(QtCore.QRect(180, 170, 171, 20))
        self.username_edit.setObjectName(_fromUtf8("username_edit"))
        ############################################################
        self.password_edit = QtGui.QLineEdit(Dialog)
        self.password_edit.setGeometry(QtCore.QRect(180, 200, 171, 20))
        self.password_edit.setObjectName(_fromUtf8("password_edit"))
        ############################################################
        self.email_edit = QtGui.QLineEdit(Dialog)
        self.email_edit.setGeometry(QtCore.QRect(180, 230, 171, 20))
        self.email_edit.setObjectName(_fromUtf8("email_edit"))
        ############################################################
        self.phone_edit = QtGui.QLineEdit(Dialog)
        self.phone_edit.setGeometry(QtCore.QRect(180, 260, 171, 20))
        self.phone_edit.setObjectName(_fromUtf8("phone_edit"))
        ############################################################
        self.address_edit = QtGui.QLineEdit(Dialog)
        self.address_edit.setGeometry(QtCore.QRect(180, 290, 171, 20))
        self.address_edit.setObjectName(_fromUtf8("address_edit"))
        ############################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Account", None))
        self.pushButton.setText(_translate("Dialog", "Create Account", None))
        self.label.setText(_translate("Dialog", "Create Patient Account", None))
        self.nameLabel.setText(_translate("Dialog", "Name", None))
        self.usernameLabel.setText(_translate("Dialog", "Username", None))
        self.passwordLabel.setText(_translate("Dialog", "Password", None))
        self.emailLabel.setText(_translate("Dialog", "Email", None))
        self.phoneLabel.setText(_translate("Dialog", "Phone", None))
        self.addressLabel.setText(_translate("Dialog", "Address", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = signup_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
