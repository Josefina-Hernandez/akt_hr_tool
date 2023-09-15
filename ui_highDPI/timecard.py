# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timecard.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimeCard(object):
    def setupUi(self, TimeCard):
        TimeCard.setObjectName("TimeCard")
        TimeCard.resize(913, 750)
        TimeCard.setMinimumSize(QtCore.QSize(913, 750))
        TimeCard.setMaximumSize(QtCore.QSize(913, 750))
        TimeCard.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color:rgb(250, 250, 250);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(TimeCard)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 290, 90))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:20pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(21, 199, 1);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:30px;\n"
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
"    font-size:23pt;\n"
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
"    font-size:20pt;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 440, 290, 90))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:20pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(200, 0, 0);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:30px;\n"
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
"    font-size:22pt;\n"
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
"    font-size:20pt;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(16, 110, 330, 100))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"        background-color:rgb(245, 245, 250);\n"
"        color:rgb(0, 0, 0);\n"
"         border-radius:20px;\n"
"}")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setLineWidth(3)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setProperty("value", 27.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(410, 45, 460, 270))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("QCalendarWidget\n"
"{\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(362, 40, 20, 710))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 670, 230, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:12pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(91, 91, 138);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(62, 62, 95);\n"
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
"    background-color:rgb(55, 55, 84);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(371, 0, 550, 40))
        self.label_2.setStyleSheet("QWidget\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:10pt;\n"
"    /*字体颜色为白色*/    \n"
"    font-weight:bold;\n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(8, 88, 186);\n"
"\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(480, 330, 190, 40))
        self.textEdit.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setLineWidth(1)
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 330, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 580, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(690, 340, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(480, 580, 190, 40))
        self.textEdit_2.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_2.setLineWidth(1)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(690, 380, 190, 40))
        self.textEdit_3.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_3.setLineWidth(1)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 440, 161, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_6.setObjectName("label_6")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(690, 480, 190, 40))
        self.textEdit_4.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_4.setLineWidth(1)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 670, 270, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:12pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(91, 91, 138);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(62, 62, 95);\n"
"    padding-left:-3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:-3px;\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(55, 55, 84);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(690, 550, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_7.setObjectName("label_7")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(690, 580, 190, 40))
        self.textEdit_5.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_5.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_5.setLineWidth(1)
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 0, 90, 40))
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:10pt;\n"
"    /*字体颜色为白色*/\n"
"    font-weight:bold;    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(8, 88, 186);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(58, 58, 89);\n"
"    padding-left:-3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:-3px;\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(43, 43, 66);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 371, 230))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-color:rgb(8, 88, 186);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 170, 31))
        self.label_8.setStyleSheet("QWidget\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:11pt;\n"
"    /*字体颜色为白色*/    \n"
"    font-weight:bold;\n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(8, 88, 186);\n"
"\n"
"}\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 170, 31))
        self.label.setStyleSheet("QWidget\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:11pt;\n"
"    /*字体颜色为白色*/    \n"
"    font-weight:bold;\n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(8, 88, 186);\n"
"\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(180, 20, 180, 50))
        self.label_9.setStyleSheet("QWidget\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:13pt;\n"
"    /*字体颜色为白色*/    \n"
"    \n"
"    color:rgb(40, 40, 40);\n"
"    /*背景颜色*/  \n"
"    background-color:white;\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 550, 290, 40))
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
"    background-color:rgb(255, 108, 3);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(220, 93, 2);\n"
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
"    background-color:rgb(163, 69, 1);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 410, 330, 30))
        self.checkBox.setStyleSheet("QCheckBox{\n"
"\n"
"    color:rgb(91, 91, 138);\n"
"        font-family:Calibri;\n"
"    /*字体大小为20点*/\n"
"   font-size:11pt;\n"
"\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 670, 290, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(480, 380, 190, 40))
        self.textEdit_6.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_6.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_6.setLineWidth(1)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 380, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_10.setObjectName("label_10")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(480, 430, 190, 40))
        self.textEdit_7.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_7.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_7.setLineWidth(1)
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(400, 430, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_11.setObjectName("label_11")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(480, 480, 190, 40))
        self.textEdit_8.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_8.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_8.setLineWidth(1)
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(400, 490, 60, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_12.setObjectName("label_12")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(480, 530, 190, 40))
        self.textEdit_9.setStyleSheet("QTextEdit\n"
"\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    color:rgb(50, 50, 50);\n"
"   font-size:10pt;\n"
"    background-color:rgb(255, 251, 201);\n"
"}\n"
"")
        self.textEdit_9.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit_9.setLineWidth(1)
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 530, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel\n"
"{\n"
"    font-family:Microsoft Yahei UI;\n"
"    font-size:11pt; \n"
"    color:rgb(128, 134, 132)\n"
"}")
        self.label_13.setObjectName("label_13")
        self.frame.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lcdNumber.raise_()
        self.calendarWidget.raise_()
        self.line.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.label_6.raise_()
        self.textEdit_4.raise_()
        self.pushButton_4.raise_()
        self.label_7.raise_()
        self.textEdit_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        self.checkBox.raise_()
        self.pushButton_7.raise_()
        self.textEdit_6.raise_()
        self.label_10.raise_()
        self.textEdit_7.raise_()
        self.label_11.raise_()
        self.textEdit_8.raise_()
        self.label_12.raise_()
        self.textEdit_9.raise_()
        self.label_13.raise_()
        TimeCard.setCentralWidget(self.centralwidget)

        self.retranslateUi(TimeCard)
        QtCore.QMetaObject.connectSlotsByName(TimeCard)

    def retranslateUi(self, TimeCard):
        _translate = QtCore.QCoreApplication.translate
        TimeCard.setWindowTitle(_translate("TimeCard", "Time Card"))
        self.pushButton.setText(_translate("TimeCard", "CLOCK IN"))
        self.pushButton_2.setText(_translate("TimeCard", "CLOCK OUT"))
        self.pushButton_3.setText(_translate("TimeCard", "Forget Record"))
        self.label_2.setText(_translate("TimeCard", "Current Date:"))
        self.label_3.setText(_translate("TimeCard", "Clock In"))
        self.label_4.setText(_translate("TimeCard", "Clock Out"))
        self.label_5.setText(_translate("TimeCard", "Work Time"))
        self.label_6.setText(_translate("TimeCard", "Over Time"))
        self.pushButton_4.setText(_translate("TimeCard", "Export Monthly Data"))
        self.label_7.setText(_translate("TimeCard", "Approved OT"))
        self.pushButton_6.setText(_translate("TimeCard", "Back"))
        self.label_8.setText(_translate("TimeCard", "CURRENT DATE:"))
        self.label.setText(_translate("TimeCard", "CURRENT TIME:"))
        self.label_9.setText(_translate("TimeCard", "20/11/2020"))
        self.pushButton_5.setText(_translate("TimeCard", "Cancel Clock Out"))
        self.checkBox.setText(_translate("TimeCard", "Clock-out for yesterday(after 0:00 am)"))
        self.pushButton_7.setText(_translate("TimeCard", "Apply Late Clock In"))
        self.label_10.setText(_translate("TimeCard", "Out-1"))
        self.label_11.setText(_translate("TimeCard", "In-1"))
        self.label_12.setText(_translate("TimeCard", "Out-2"))
        self.label_13.setText(_translate("TimeCard", "In-2"))
