# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/qtz-robot/pyqt_test/photos sharing/server/windows/photo_exchange.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 6, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_4.addWidget(self.line_6, 6, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 4, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_3.addWidget(self.line_8)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 25pt \"Ubuntu\";\n"
"color: rgb(204, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.port = QtWidgets.QLineEdit(self.centralwidget)
        self.port.setObjectName("port")
        self.horizontalLayout_2.addWidget(self.port)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(15, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ip = QtWidgets.QLineEdit(self.centralwidget)
        self.ip.setObjectName("ip")
        self.horizontalLayout.addWidget(self.ip)
        self.sutoip = QtWidgets.QPushButton(self.centralwidget)
        self.sutoip.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.sutoip.setObjectName("sutoip")
        self.horizontalLayout.addWidget(self.sutoip)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.start.setObjectName("start")
        self.horizontalLayout_5.addWidget(self.start)
        self.disconn = QtWidgets.QPushButton(self.centralwidget)
        self.disconn.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.disconn.setObjectName("disconn")
        self.horizontalLayout_5.addWidget(self.disconn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_8.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setObjectName("path")
        self.horizontalLayout_4.addWidget(self.path)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.rename = QtWidgets.QLineEdit(self.centralwidget)
        self.rename.setObjectName("rename")
        self.horizontalLayout_4.addWidget(self.rename)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.selectsave = QtWidgets.QPushButton(self.centralwidget)
        self.selectsave.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.selectsave.setObjectName("selectsave")
        self.horizontalLayout_13.addWidget(self.selectsave)
        self.savepicbtn = QtWidgets.QPushButton(self.centralwidget)
        self.savepicbtn.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.savepicbtn.setObjectName("savepicbtn")
        self.horizontalLayout_13.addWidget(self.savepicbtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.selectsend = QtWidgets.QPushButton(self.centralwidget)
        self.selectsend.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.selectsend.setObjectName("selectsend")
        self.horizontalLayout_7.addWidget(self.selectsend)
        self.sendpic = QtWidgets.QPushButton(self.centralwidget)
        self.sendpic.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.sendpic.setObjectName("sendpic")
        self.horizontalLayout_7.addWidget(self.sendpic)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.sendpath = QtWidgets.QLineEdit(self.centralwidget)
        self.sendpath.setObjectName("sendpath")
        self.horizontalLayout_7.addWidget(self.sendpath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_8.addWidget(self.line_10)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 5, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 558, 465))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image.setStyleSheet("font: 75 36pt \"微软雅黑\";")
        self.image.setObjectName("image")
        self.gridLayout_3.addWidget(self.image, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 4, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scale_2 = QtWidgets.QLabel(self.centralwidget)
        self.scale_2.setObjectName("scale_2")
        self.horizontalLayout_6.addWidget(self.scale_2)
        self.scale = QtWidgets.QLabel(self.centralwidget)
        self.scale.setObjectName("scale")
        self.horizontalLayout_6.addWidget(self.scale)
        self.scaleSlider = QtWidgets.QSlider(self.centralwidget)
        self.scaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.scaleSlider.setObjectName("scaleSlider")
        self.horizontalLayout_6.addWidget(self.scaleSlider)
        self.enlage = QtWidgets.QPushButton(self.centralwidget)
        self.enlage.setObjectName("enlage")
        self.horizontalLayout_6.addWidget(self.enlage)
        self.reduce = QtWidgets.QPushButton(self.centralwidget)
        self.reduce.setObjectName("reduce")
        self.horizontalLayout_6.addWidget(self.reduce)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.up = QtWidgets.QPushButton(self.centralwidget)
        self.up.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.up.setObjectName("up")
        self.horizontalLayout_9.addWidget(self.up)
        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.down.setObjectName("down")
        self.horizontalLayout_9.addWidget(self.down)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.picdata = QtWidgets.QTextEdit(self.tab_2)
        self.picdata.setObjectName("picdata")
        self.gridLayout_2.addWidget(self.picdata, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.tabWidget_2, 0, 1, 4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " 图 片 互 传 "))
        self.label_3.setText(_translate("MainWindow", "Port："))
        self.port.setText(_translate("MainWindow", "8899"))
        self.label_2.setText(_translate("MainWindow", "Ip："))
        self.sutoip.setText(_translate("MainWindow", "自动识别"))
        self.start.setText(_translate("MainWindow", "启动"))
        self.disconn.setText(_translate("MainWindow", "断开连接"))
        self.label_5.setText(_translate("MainWindow", "Save_Path："))
        self.label_6.setText(_translate("MainWindow", "重命名图片："))
        self.selectsave.setText(_translate("MainWindow", "选择保存路径"))
        self.savepicbtn.setText(_translate("MainWindow", "保存图片"))
        self.selectsend.setText(_translate("MainWindow", "选择发送图片"))
        self.sendpic.setText(_translate("MainWindow", "发送图片"))
        self.label_8.setText(_translate("MainWindow", "Send_Path："))
        self.image.setText(_translate("MainWindow", "           NO IMAGE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "图片显示框"))
        self.scale_2.setText(_translate("MainWindow", "放大倍数："))
        self.scale.setText(_translate("MainWindow", "0.0%"))
        self.enlage.setText(_translate("MainWindow", "放大"))
        self.reduce.setText(_translate("MainWindow", "缩小"))
        self.up.setText(_translate("MainWindow", "上一张"))
        self.down.setText(_translate("MainWindow", "下一张"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "图片数据及传输信息"))