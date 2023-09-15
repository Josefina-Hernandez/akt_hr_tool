# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team_structure.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeamStructure(object):
    def setupUi(self, TeamStructure):
        TeamStructure.setObjectName("TeamStructure")
        TeamStructure.resize(1272, 724)
        TeamStructure.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color: rgb(255, 251, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(TeamStructure)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"\n"
"    font-size:13pt;\n"
" \n"
"    color:white;\n"
"\n"
"    background-color:rgb(21, 199, 1);\n"
"\n"
"    border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(21, 175, 0);\n"
"    padding-left:-3px;\n"
"    padding-top:-3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{  \n"
"    background-color:rgb(0, 113, 0);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:13pt; \n"
"    color:white;\n"
"    background-color:rgb(255, 170, 0);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(230, 153, 0);\n"
"    padding-left:-3px;\n"
"    padding-top:-3px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(197, 128, 0);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:13pt;  \n"
"    color:white;\n"
"    background-color:rgb(200, 0, 0);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color:rgb(176, 0, 0);\n"
"    padding-left:-3px;\n"
"    padding-top:-3px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(147, 0, 0);  \n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    font-size:13pt;}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        TeamStructure.setCentralWidget(self.centralwidget)

        self.retranslateUi(TeamStructure)
        QtCore.QMetaObject.connectSlotsByName(TeamStructure)

    def retranslateUi(self, TeamStructure):
        _translate = QtCore.QCoreApplication.translate
        TeamStructure.setWindowTitle(_translate("TeamStructure", "Steam Structure"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TeamStructure", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TeamStructure", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TeamStructure", "POSITION"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TeamStructure", "DIVISION"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TeamStructure", "LEADER ID"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("TeamStructure", "LEADER NAME"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("TeamStructure", "DM ID"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("TeamStructure", "DM NAME"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("TeamStructure", "MD ID"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("TeamStructure", "MD NAME"))
        self.pushButton_2.setText(_translate("TeamStructure", "Export Excel List"))
        self.pushButton_3.setText(_translate("TeamStructure", "Import Excel List"))
        self.pushButton_4.setText(_translate("TeamStructure", "Resume"))
