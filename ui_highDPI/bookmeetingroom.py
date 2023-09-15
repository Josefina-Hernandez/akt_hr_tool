# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookmeetingroom.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookMeetingRoom(object):
    def setupUi(self, BookMeetingRoom):
        BookMeetingRoom.setObjectName("BookMeetingRoom")
        BookMeetingRoom.resize(1386, 781)
        BookMeetingRoom.setMinimumSize(QtCore.QSize(1386, 781))
        BookMeetingRoom.setMaximumSize(QtCore.QSize(1386, 781))
        BookMeetingRoom.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color: rgb(239, 255, 237);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(BookMeetingRoom)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 20, 421, 261))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(10, 290, 290, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(111,111,111);\n"
"}")
        self.label_24.setObjectName("label_24")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(420, 20, 961, 660))
        self.tableWidget.setStyleSheet("QTableWidget\n"
"{\n"
"    background-color: rgb(225, 255, 254);\n"
"\n"
"}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(36, 236, 239))
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1390, 16))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-color:rgb(8, 88, 186);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(20, 330, 140, 40))
        self.timeEdit.setStyleSheet("QTimeEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(77,77,77);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"QTimeEdit:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}\n"
"\n"
"QTimeEdit:focus\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}")
        self.timeEdit.setAccelerated(True)
        self.timeEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit.setProperty("showGroupSeparator", True)
        self.timeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 3), QtCore.QTime(0, 0, 0)))
        self.timeEdit.setDisplayFormat("hh:mm")
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(250, 330, 140, 40))
        self.timeEdit_2.setStyleSheet("QTimeEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(77,77,77);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"QTimeEdit:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}\n"
"\n"
"QTimeEdit:focus\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}")
        self.timeEdit_2.setAccelerated(True)
        self.timeEdit_2.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit_2.setProperty("showGroupSeparator", True)
        self.timeEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 3), QtCore.QTime(0, 0, 0)))
        self.timeEdit_2.setDisplayFormat("hh:mm")
        self.timeEdit_2.setCalendarPopup(True)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(160, 340, 90, 16))
        self.line_10.setStyleSheet("Line\n"
"{\n"
"    color:rgb(0, 0, 255);\n"
"}")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 700, 380, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:13pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(21, 199, 1);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(21, 175, 0);\n"
"    padding-left:-3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:-3px;\n"
"\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(0, 113, 0);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 700, 380, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:13pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(255, 170, 0);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(230, 153, 0);\n"
"    padding-left:-3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:-3px;\n"
"\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(197, 128, 0);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(10, 490, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(111,111,111);\n"
"}")
        self.label_25.setObjectName("label_25")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 530, 380, 150))
        self.textEdit.setStyleSheet("QTextEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(74, 74, 74);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextEdit:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(33, 360, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(229, 0, 0)\n"
"}")
        self.label_31.setObjectName("label_31")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1300, 700, 70, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:13pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(200, 0, 0);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(176, 0, 0);\n"
"    padding-left:-3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:-3px;\n"
"     font-size:15pt;\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(147, 0, 0);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"    font-size:13pt;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(10, 410, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(111,111,111);\n"
"}")
        self.label_26.setObjectName("label_26")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 440, 191, 21))
        self.radioButton.setStyleSheet("QRadioButton{\n"
"\n"
"      color:rgb(91, 91, 138);\n"
"      font-family:Calibri;\n"
"      font-size:11pt;\n"
"      font-weight: bold;\n"
"\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 440, 161, 21))
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"\n"
"      color:rgb(91, 91, 138);\n"
"      font-family:Calibri;\n"
"      font-size:11pt;\n"
"      font-weight: bold;\n"
"\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(310, 440, 101, 21))
        self.radioButton_3.setStyleSheet("QRadioButton{\n"
"\n"
"      color:rgb(91, 91, 138);\n"
"      font-family:Calibri;\n"
"      font-size:11pt;\n"
"      font-weight: bold;\n"
"\n"
"}")
        self.radioButton_3.setObjectName("radioButton_3")
        BookMeetingRoom.setCentralWidget(self.centralwidget)

        self.retranslateUi(BookMeetingRoom)
        QtCore.QMetaObject.connectSlotsByName(BookMeetingRoom)

    def retranslateUi(self, BookMeetingRoom):
        _translate = QtCore.QCoreApplication.translate
        BookMeetingRoom.setWindowTitle(_translate("BookMeetingRoom", "Book Meeting Room"))
        self.label_24.setText(_translate("BookMeetingRoom", "Please Select Time Range:"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BookMeetingRoom", "Booking ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BookMeetingRoom", "Room No."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BookMeetingRoom", "Meeting Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BookMeetingRoom", "Start Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("BookMeetingRoom", "Finish Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BookMeetingRoom", "Applier"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("BookMeetingRoom", "Division"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("BookMeetingRoom", "Meeting Contents"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("BookMeetingRoom", "Book Meeting Room"))
        self.pushButton_4.setText(_translate("BookMeetingRoom", "Cancel Selected Booking"))
        self.label_25.setText(_translate("BookMeetingRoom", "Meeting Contents:"))
        self.label_31.setText(_translate("BookMeetingRoom", "Please input the correct time range!"))
        self.pushButton_5.setText(_translate("BookMeetingRoom", "X"))
        self.label_26.setText(_translate("BookMeetingRoom", "Meeting Room:"))
        self.radioButton.setText(_translate("BookMeetingRoom", "Room 1"))
        self.radioButton_2.setText(_translate("BookMeetingRoom", "Room 2 (Kitchen)"))
        self.radioButton_3.setText(_translate("BookMeetingRoom", "Room 3"))
