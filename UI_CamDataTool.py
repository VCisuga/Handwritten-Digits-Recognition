# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_CamDataTool.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

# import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Window_CamDataTool(object):
    def setupUi(self, Window_CamDataTool):
        Window_CamDataTool.setObjectName("Window_CamDataTool")
        Window_CamDataTool.resize(640, 317)
        self.centralwidget = QtWidgets.QWidget(Window_CamDataTool)
        self.centralwidget.setObjectName("centralwidget")
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(10, 19, 111, 21))
        self.label_file.setObjectName("label_file")
        self.lineEdit_prnum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prnum.setEnabled(True)
        self.lineEdit_prnum.setGeometry(QtCore.QRect(120, 100, 71, 20))
        self.lineEdit_prnum.setObjectName("lineEdit_prnum")
        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.label_data.setObjectName("label_data")
        self.label_pr = QtWidgets.QLabel(self.centralwidget)
        self.label_pr.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_pr.setObjectName("label_pr")
        self.lineEdit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filename.setEnabled(False)
        self.lineEdit_filename.setGeometry(QtCore.QRect(120, 19, 281, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(6)
        self.lineEdit_filename.setFont(font)
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(410, 19, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")
        self.comboBox_data = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_data.setGeometry(QtCore.QRect(120, 60, 351, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.comboBox_data.setFont(font)
        self.comboBox_data.setObjectName("comboBox_data")
        self.pushButton_activate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_activate.setGeometry(QtCore.QRect(400, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_activate.setFont(font)
        self.pushButton_activate.setStyleSheet("color: rgb(0, 0, 255);")
        self.pushButton_activate.setObjectName("pushButton_activate")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setEnabled(False)
        self.pushButton_send.setGeometry(QtCore.QRect(520, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_send.setFont(font)
        self.pushButton_send.setStyleSheet("color: rgb(0, 170, 0);")
        self.pushButton_send.setObjectName("pushButton_send")
        self.textEdit_log = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_log.setEnabled(True)
        self.textEdit_log.setGeometry(QtCore.QRect(10, 140, 371, 111))
        self.textEdit_log.setObjectName("textEdit_log")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(400, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_sendall = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sendall.setEnabled(False)
        self.pushButton_sendall.setGeometry(QtCore.QRect(520, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_sendall.setFont(font)
        self.pushButton_sendall.setStyleSheet("color: rgb(0, 170, 0);")
        self.pushButton_sendall.setObjectName("pushButton_sendall")
        self.pushButton_autosend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_autosend.setEnabled(True)
        self.pushButton_autosend.setGeometry(QtCore.QRect(400, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_autosend.setFont(font)
        self.pushButton_autosend.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_autosend.setObjectName("pushButton_autosend")
        Window_CamDataTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window_CamDataTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        Window_CamDataTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window_CamDataTool)
        self.statusbar.setObjectName("statusbar")
        Window_CamDataTool.setStatusBar(self.statusbar)

        self.retranslateUi(Window_CamDataTool)
        QtCore.QMetaObject.connectSlotsByName(Window_CamDataTool)

    def retranslateUi(self, Window_CamDataTool):
        _translate = QtCore.QCoreApplication.translate
        Window_CamDataTool.setWindowTitle(_translate("Window_CamDataTool", "相机数据处理辅助工具"))
        self.label_file.setText(_translate("Window_CamDataTool", "选择相机数据文件："))
        self.label_data.setText(_translate("Window_CamDataTool", "发送数据："))
        self.label_pr.setText(_translate("Window_CamDataTool", "PR寄存器地址："))
        self.pushButton_open.setText(_translate("Window_CamDataTool", "打开文件"))
        self.pushButton_activate.setText(_translate("Window_CamDataTool", "启动线程"))
        self.pushButton_send.setText(_translate("Window_CamDataTool", "发送数据"))
        self.pushButton_close.setText(_translate("Window_CamDataTool", "关闭线程"))
        self.pushButton_sendall.setText(_translate("Window_CamDataTool", "发送全部"))
        self.pushButton_autosend.setText(_translate("Window_CamDataTool", "自动发送"))


# if __name__ == '__main__':
#     App = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
#     aw = Ui_Window_CamDataTool()  # 创建主窗体对象，实例化Ui_MainWindow
#     w = QMainWindow()  # 实例化QMainWindow类
#     aw.setupUi(w)  # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
#     w.show()  # 显示主窗体
#     # App.exit()
#     sys.exit(App.exec_())  # 循环中等待退出程序
