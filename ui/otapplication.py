# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otapplication.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OTApplication(object):
    def setupUi(self, OTApplication):
        OTApplication.setObjectName("OTApplication")
        OTApplication.resize(858, 526)
        OTApplication.setMinimumSize(QtCore.QSize(858, 526))
        OTApplication.setMaximumSize(QtCore.QSize(858, 526))
        self.centralwidget = QtWidgets.QWidget(OTApplication)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 851, 511))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget\n"
"{\n"
"    background-color: rgb(243, 247, 255)\n"
"\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(20, 20, 151, 31))
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
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_3.setGeometry(QtCore.QRect(20, 50, 241, 41))
        self.dateEdit_3.setStyleSheet("QDateEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(74, 74, 74);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255,255);\n"
"}\n"
"\n"
"QDateEdit:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}")
        self.dateEdit_3.setWrapping(False)
        self.dateEdit_3.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_3.setDisplayFormat("dd/MM/yyyy")
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(20, 110, 151, 31))
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
        self.timeEdit = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit.setGeometry(QtCore.QRect(20, 140, 241, 41))
        self.timeEdit.setStyleSheet("QTimeEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(74, 74, 74);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
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
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 2), QtCore.QTime(1, 0, 0)))
        self.timeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 2), QtCore.QTime(0, 0, 0)))
        self.timeEdit.setDisplayFormat("hh:mm")
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(20, 200, 151, 31))
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
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit_2.setGeometry(QtCore.QRect(20, 230, 241, 41))
        self.timeEdit_2.setStyleSheet("QTimeEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(74, 74, 74);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
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
        self.timeEdit_2.setDisplayFormat("hh:mm")
        self.timeEdit_2.setCalendarPopup(True)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(20, 290, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(111,111,111);\n"
"}")
        self.label_27.setObjectName("label_27")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 320, 241, 41))
        self.textEdit_5.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_5.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_5.setLineWidth(1)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(320, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(111,111,111);\n"
"}")
        self.label_28.setObjectName("label_28")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(320, 50, 470, 90))
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
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 410, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
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
        self.pushButton.setObjectName("pushButton")
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(610, 307, 40, 16))
        self.line_5.setStyleSheet("Line\n"
"{\n"
"    color:rgb(0, 0, 255);\n"
"}")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(330, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 11pt;\n"
"    color:rgb(0, 170, 0);\n"
"}")
        self.label_20.setObjectName("label_20")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(330, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 11pt;\n"
"    color:rgb(0, 170, 0);\n"
"}")
        self.label_11.setObjectName("label_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 240, 160, 22))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("QComboBox\n"
"    {font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:grey;\n"
"   font-size:12pt;\n"
"\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}\n"
"\n"
"QComboBox:focus\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(330, 270, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 11pt;\n"
"    color:rgb(0, 170, 0);\n"
"}")
        self.label_14.setObjectName("label_14")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(520, 307, 40, 16))
        self.line_2.setStyleSheet("Line\n"
"{\n"
"    color:rgb(0, 0, 255);\n"
"}")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(438, 308, 40, 16))
        self.line.setStyleSheet("Line\n"
"{\n"
"    color:rgb(0, 0, 255);\n"
"}")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(570, 300, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(0, 0, 255)\n"
"}")
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(480, 300, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(0, 0, 255)\n"
"}")
        self.label_15.setObjectName("label_15")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(660, 300, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(0, 0, 255)\n"
"}")
        self.label_22.setObjectName("label_22")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(370, 300, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(0, 0, 255)\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(430, 370, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(255, 170, 0)\n"
"}")
        self.label_21.setObjectName("label_21")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(320, 170, 470, 310))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-color:rgb(255, 250, 220);\n"
"    border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 250, 240, 30))
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 0, 121, 30))
        self.checkBox.setStyleSheet("QCheckBox\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:10pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:rgb(0,76,10);\n"
"    /*背景颜色*/  \n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QCheckBox:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(21, 175, 0);\n"
"    font-size:14pt;\n"
"    padding-left:-3px;\n"
"    font-weight:bold;\n"
"    color:white;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:-3px;\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QCheckBox:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(0, 113, 0);\n"
"    font-weight:bold;\n"
"    font-size:14pt;\n"
"    color:white;\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 160, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:20pt;\n"
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
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(197, 128, 0);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 160, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:20pt;\n"
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
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(197, 128, 0);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 160, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:20pt;\n"
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
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(197, 128, 0);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 160, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:20pt;\n"
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
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(197, 128, 0);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(210, 40, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 11pt;\n"
"    color:rgb(0, 170, 0);\n"
"}")
        self.label_12.setObjectName("label_12")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_4.setGeometry(QtCore.QRect(240, 70, 170, 22))
        self.dateEdit_4.setStyleSheet("QDateEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(74, 74, 74);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}")
        self.dateEdit_4.setWrapping(False)
        self.dateEdit_4.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_4.setDisplayFormat("dd/MM/yyyy")
        self.dateEdit_4.setCalendarPopup(True)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(10, 380, 270, 30))
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
        self.frame.raise_()
        self.label_24.raise_()
        self.dateEdit_3.raise_()
        self.label_25.raise_()
        self.timeEdit.raise_()
        self.label_26.raise_()
        self.timeEdit_2.raise_()
        self.label_27.raise_()
        self.textEdit_5.raise_()
        self.label_28.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.line_5.raise_()
        self.label_20.raise_()
        self.label_11.raise_()
        self.comboBox_2.raise_()
        self.label_14.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.label_16.raise_()
        self.label_15.raise_()
        self.label_22.raise_()
        self.label_13.raise_()
        self.label_21.raise_()
        self.label_31.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 831, 370))
        self.tableWidget.setStyleSheet("QTableWidget\n"
"{\n"
"    background-color: rgb(225, 255, 254);\n"
"\n"
"}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(14)
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
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(11, 5, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(111,111,111);\n"
"}")
        self.label_29.setObjectName("label_29")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setGeometry(QtCore.QRect(50, 10, 121, 21))
        self.dateEdit.setStyleSheet("QDateEdit\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(74, 74, 74);\n"
"   font-size:12pt;\n"
"    background-color:rgb(255, 255,255);\n"
"}\n"
"\n"
"QDateEdit:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}\n"
"\n"
"QDateEdit:focus\n"
"{\n"
"    /*背景颜色*/  \n"
"   background-color:rgb(229, 242, 255);\n"
"}")
        self.dateEdit.setDisplayFormat("yyyy")
        self.dateEdit.setObjectName("dateEdit")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(200, 4, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel\n"
"{\n"
"    font-size:11pt;\n"
"    color:rgb(111,111,111);\n"
"}")
        self.label_30.setObjectName("label_30")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(260, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("QComboBox\n"
"\n"
"    {font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:color:rgb(74, 74, 74);\n"
"   font-size:12pt;\n"
"\n"
"}\n"
"")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_3.setFrame(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 420, 280, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 420, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_16.setGeometry(QtCore.QRect(640, 10, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:9pt;\n"
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
"    font-size:10pt;\n"
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
"    font-size:9pt;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 450, 40, 40))
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 861, 16))
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"    background-color:rgb(14 , 150 , 254);\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        OTApplication.setCentralWidget(self.centralwidget)

        self.retranslateUi(OTApplication)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(-1)
        self.comboBox_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OTApplication)

    def retranslateUi(self, OTApplication):
        _translate = QtCore.QCoreApplication.translate
        OTApplication.setWindowTitle(_translate("OTApplication", "OT Application"))
        self.label_24.setText(_translate("OTApplication", "Date of OT"))
        self.label_25.setText(_translate("OTApplication", "Start From"))
        self.label_26.setText(_translate("OTApplication", "Until"))
        self.label_27.setText(_translate("OTApplication", "OT Hour(s)"))
        self.label_28.setText(_translate("OTApplication", "Remarks"))
        self.pushButton.setText(_translate("OTApplication", "APPLY FOR OT"))
        self.label_20.setText(_translate("OTApplication", "Status:"))
        self.label_11.setText(_translate("OTApplication", "Request ID:"))
        self.label_14.setText(_translate("OTApplication", "Approved by:"))
        self.label_16.setText(_translate("OTApplication", "HR"))
        self.label_15.setText(_translate("OTApplication", "DM"))
        self.label_22.setText(_translate("OTApplication", "MD"))
        self.label_13.setText(_translate("OTApplication", "Leader"))
        self.label_21.setText(_translate("OTApplication", "WAITING..."))
        self.pushButton_5.setText(_translate("OTApplication", "CANCEL REQUEST"))
        self.checkBox.setText(_translate("OTApplication", "Request Query"))
        self.pushButton_8.setText(_translate("OTApplication", "―"))
        self.pushButton_9.setText(_translate("OTApplication", "―"))
        self.pushButton_10.setText(_translate("OTApplication", "―"))
        self.pushButton_11.setText(_translate("OTApplication", "―"))
        self.label_12.setText(_translate("OTApplication", "Date of OT:"))
        self.label_31.setText(_translate("OTApplication", "Please input the correct time range!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("OTApplication", "OT application"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("OTApplication", "Request ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("OTApplication", "User ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("OTApplication", "User Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("OTApplication", "Request DTTM"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("OTApplication", "Request DT"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("OTApplication", "Date of OT"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("OTApplication", "Start Time"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("OTApplication", "End Time"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("OTApplication", "OT Hours"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("OTApplication", "Leader"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("OTApplication", "DM"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("OTApplication", "HR"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("OTApplication", "MD"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("OTApplication", "Remarks"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_29.setText(_translate("OTApplication", "Year"))
        self.label_30.setText(_translate("OTApplication", "Month"))
        self.comboBox_3.setCurrentText(_translate("OTApplication", "01"))
        self.comboBox_3.setItemText(0, _translate("OTApplication", "01"))
        self.comboBox_3.setItemText(1, _translate("OTApplication", "02"))
        self.comboBox_3.setItemText(2, _translate("OTApplication", "03"))
        self.comboBox_3.setItemText(3, _translate("OTApplication", "04"))
        self.comboBox_3.setItemText(4, _translate("OTApplication", "05"))
        self.comboBox_3.setItemText(5, _translate("OTApplication", "06"))
        self.comboBox_3.setItemText(6, _translate("OTApplication", "07"))
        self.comboBox_3.setItemText(7, _translate("OTApplication", "08"))
        self.comboBox_3.setItemText(8, _translate("OTApplication", "09"))
        self.comboBox_3.setItemText(9, _translate("OTApplication", "10"))
        self.comboBox_3.setItemText(10, _translate("OTApplication", "11"))
        self.comboBox_3.setItemText(11, _translate("OTApplication", "12"))
        self.comboBox_3.setItemText(12, _translate("OTApplication", "All"))
        self.pushButton_6.setText(_translate("OTApplication", "Cancel Selected Request"))
        self.pushButton_2.setText(_translate("OTApplication", "Export to Excel File"))
        self.pushButton_16.setText(_translate("OTApplication", "Click To Show Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("OTApplication", "Summary"))
        self.pushButton_4.setText(_translate("OTApplication", "X"))
