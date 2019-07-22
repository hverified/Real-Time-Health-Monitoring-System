# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctorPage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from dateutil import parser
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from signup import signup_Dialog

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

class doctor_page(object):
    def showAlert(self,title,message):
        msgBox = QtGui.QMessageBox()
        #msgBox.setIcon(msgBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(msgBox.Ok)
        msgBox.exec_()
    def addPatient(self):
        self.signupwindow = QtGui.QDialog()
        self.ui = signup_Dialog()
        self.ui.setupUi(self.signupwindow)
        self.signupwindow.show()

    def patient_record(self):
        name = self.nameEdit.text()
        username = self.usernameEdit.text()

        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        result = c.execute('SELECT * FROM login WHERE Name = ? AND Username = ?',(name,username))
        conn.commit()
        if len(result.fetchall()) > 0:

            fig = plt.figure()
            ax1 = fig.add_subplot(1,1,1)

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
                ax1.clear()
                ax1.plot(timestamp, temp)

                conn.commit()
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()
        else:
            self.showAlert('Warning','User does not exists')


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(482, 484)
        Dialog.setStyleSheet(_fromUtf8("QDialog{background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 rgba(41, 156, 255, 255), stop:1 rgba(255, 255, 255, 255));}"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 90, 211, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.seePatientBtn = QtGui.QPushButton(Dialog)
        self.seePatientBtn.setGeometry(QtCore.QRect(190, 250, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.seePatientBtn.setFont(font)
        self.seePatientBtn.setObjectName(_fromUtf8("seePatientBtn"))
        self.seePatientBtn.clicked.connect(self.patient_record)

        self.nameEdit = QtGui.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(230, 180, 200, 21))
        self.nameEdit.setObjectName(_fromUtf8("lineEdit"))
        self.usernameEdit = QtGui.QLineEdit(Dialog)
        self.usernameEdit.setGeometry(QtCore.QRect(230, 210, 200, 21))
        self.usernameEdit.setObjectName(_fromUtf8("lineEdit"))

        self.addPatientBtn = QtGui.QPushButton(Dialog)
        self.addPatientBtn.setGeometry(QtCore.QRect(190, 300, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.addPatientBtn.setFont(font)
        self.addPatientBtn.setObjectName(_fromUtf8("addPatientBtn"))
        self.addPatientBtn.clicked.connect(self.addPatient)

        self.nameLabel = QtGui.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(70, 180, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName(_fromUtf8("label_2"))

        self.usernameLabel = QtGui.QLabel(Dialog)
        self.usernameLabel.setGeometry(QtCore.QRect(70, 210, 150, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(11)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Doctor Page", None))
        self.label.setText(_translate("Dialog", "Doctor Page", None))
        self.seePatientBtn.setText(_translate("Dialog", "See Patient Record", None))
        self.addPatientBtn.setText(_translate("Dialog", "Add New patient", None))
        self.nameLabel.setText(_translate("Dialog", "Patient Name", None))
        self.usernameLabel.setText(_translate("Dialog", "Patient Username", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = doctor_page()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
