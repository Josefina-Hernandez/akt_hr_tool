# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tip_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tipwindow(object):
    def setupUi(self, Tipwindow):
        Tipwindow.setObjectName("Tipwindow")
        Tipwindow.resize(400, 300)
        Tipwindow.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.label = QtWidgets.QLabel(Tipwindow)
        self.label.setGeometry(QtCore.QRect(20, 110, 360, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    color:#9D0B0F;\n"
"    font-size: 10pt;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Tipwindow)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 420, 20))
        self.label_2.setStyleSheet("QWidget\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:15pt;\n"
"    /*字体颜色为白色*/    \n"
"    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:#EC1C24;\n"
"\n"
"}\n"
"")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Tipwindow)
        self.widget.setGeometry(QtCore.QRect(80, 240, 210, 50))
        self.widget.setStyleSheet("\n"
"background-image: url(:/source/AKT_logo.png);\n"
"")
        self.widget.setObjectName("widget")

        self.retranslateUi(Tipwindow)
        QtCore.QMetaObject.connectSlotsByName(Tipwindow)

    def retranslateUi(self, Tipwindow):
        _translate = QtCore.QCoreApplication.translate
        Tipwindow.setWindowTitle(_translate("Tipwindow", "Tip"))
        self.label.setText(_translate("Tipwindow", "Tip window"))
import ui_highDPI.Logo_AKT_rc