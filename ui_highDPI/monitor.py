# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(980, 188)
        Monitor.setMinimumSize(QtCore.QSize(980, 188))
        Monitor.setMaximumSize(QtCore.QSize(980, 188))
        Monitor.setStyleSheet("QWidget{\n"
"\n"
"    background-color:rgb(250, 250, 250);\n"
"\n"
"}")
        self.progressBar = QtWidgets.QProgressBar(Monitor)
        self.progressBar.setGeometry(QtCore.QRect(47, 90, 901, 31))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"\n"
"    color: rgb(0, 131, 0);\n"
"    font-size: 12pt;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Monitor)
        self.label.setGeometry(QtCore.QRect(47, 50, 891, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(13, 184, 39);\n"
"    font-size: 10pt;\n"
"}")
        self.label.setObjectName("label")

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Status Monitor"))
        self.label.setText(_translate("Monitor", "Creating OT Sheet for"))
