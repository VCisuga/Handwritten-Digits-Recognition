# -*- coding:utf-8 -*-

import sys
import socket
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(1000, 600)
        self.setWindowTitle("显示图像")

        self.label = QLabel(self)
        self.label.setText("随机图像")
        self.label.setFixedSize(400, 400)  # 设置大小
        self.label.move(100, 150)  # 设置位置

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:16px;font-weight:bold;font-family:宋体;}"
                                 )

        self.setWindowTitle("随机图像识别")

        self.label2 = QLabel(self)
        self.label2.setText("识别结果")
        self.label2.setFixedSize(500, 100)
        self.label2.move(530, 150)

        self.label2.setStyleSheet("QLabel{background:white;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:16px;font-weight:bold;font-family:宋体;}"
                                  )

        btn = QPushButton(self)
        btn.setText("图片识别")
        btn.move(10, 30)
        btn.clicked.connect(self.start)

    def start(self):
        CLI_HOST = 'localhost'
        CLI_PORT = 6601
        CLI_ADDR = (CLI_HOST, CLI_PORT)
        BUFSIZE = 1024

        while True:
            sock = socket.socket()
            try:
                a = sock.connect(CLI_ADDR)
            except Exception as e:
                print('error', e)
                sock.close()
                sys.exit()
            else:
                print('have connected with server')
                data = str(np.random.randint(1, 31))
                self.openimage(data)
                if len(data) > 0:
                    print('send:', data)
                    sock.sendall(data.encode())  # 不要用send()
                    recv_data = sock.recv(BUFSIZE)
                    self.label2.setText(recv_data.decode())
                    # sock.close()
                    break
                else:
                    # sock.close()
                    self.label2.setText('生成随机数字失败')
                    break


    def openimage(self, data):
        imgName = './image_archive/' + data + '.bmp'
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())