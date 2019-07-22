# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#from signup import Ui_Dialog2
import sqlite3
from dateutil import parser
import matplotlib.animation as animation
import matplotlib.pyplot as plt

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

class login_Dialog(object):
    def showAlert(self,title,message):
        msgBox = QtGui.QMessageBox()
        #msgBox.setIcon(msgBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(msgBox.Ok)
        msgBox.exec_()

    def logincheck(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        result = c.execute('SELECT * FROM login WHERE USERNAME = ? AND PASSWORD = ?',(username,password))
        conn.commit()
        if len(result.fetchall()) > 0:

            fig = plt.figure()
            fig.suptitle('Real time plot of temperature and emg')

            ax2 = fig.add_subplot(2,1,1)
            ax1 = fig.add_subplot(2,1,2)
            #plt.style.use('dark_background')

            def animate(i):
                c.execute("SELECT * FROM "+username)

                rows = c.fetchall()
                temp = []
                timestamp = []
                timestamp_s = []
                emg = []

                for row in rows:
                    temp.append(row[1])
                    timestamp_s.append(row[0])
                    emg.append(row[2])
                for time in timestamp_s:
                    timestamp.append(parser.parse(time))

                print(temp, timestamp, emg)

                ax1 = fig.add_subplot(2,1,1)
                plt.ylabel('Temperature')
                ax2 = fig.add_subplot(2,1,2)
                plt.ylabel('EMG')

                plt.xlabel('Time')
                ax1.plot(timestamp, temp, 'r')

                ax2.plot(timestamp, emg, 'b')
                #ax1.clear()
                #ax2.clear()

                conn.commit()
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()



        else:
            self.showAlert('Warning','User does not exists')

    '''def signuppage(self):
        self.signupwindow = QtGui.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.signupwindow)
        self.signupwindow.show()'''

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(481, 485)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 rgba(41, 156, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 80, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.username_edit = QtGui.QLineEdit(Dialog)
        self.username_edit.setGeometry(QtCore.QRect(200, 190, 141, 20))
        self.username_edit.setObjectName(_fromUtf8("username_edit"))
        self.password_edit = QtGui.QLineEdit(Dialog)
        self.password_edit.setGeometry(QtCore.QRect(200, 220, 141, 20))
        self.password_edit.setObjectName(_fromUtf8("password_edit"))
        self.password_edit.setEchoMode(self.password_edit.Password)
        
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(200, 280, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(10)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        ################################################################
        self.login_btn.clicked.connect(self.logincheck)
        ################################################################
        '''self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(280, 280, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(10)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        #################################################################
        self.signup_btn.clicked.connect(self.signuppage)
        #################################################################'''

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Patient Login", None))
        self.label.setText(_translate("Dialog", "Patient Login", None))
        self.label_2.setText(_translate("Dialog", "Username", None))
        self.label_3.setText(_translate("Dialog", "Password", None))
        self.login_btn.setText(_translate("Dialog", "Login", None))
        #self.signup_btn.setText(_translate("Dialog", "Sign Up", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = login_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
