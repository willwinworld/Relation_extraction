# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gui import openFile

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 347)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 80, 69, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 524, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.showMessage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "点击"))
        self.comboBox.setItemText(0, _translate("MainWindow", "北京"))
        self.comboBox.setItemText(1, _translate("MainWindow", "上海"))
        self.comboBox.setItemText(2, _translate("MainWindow", "深圳"))
        self.comboBox.setItemText(3, _translate("MainWindow", "哈尔滨"))

        #定义自己设置的函数
        def showMessage(self):
            QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        #self体现的是成员变量，实例对象，不带self是类变量，可以使用类名直接得到它的值，也可以使用实例变量
        self.another = openFile.MyWindow()
        super(MyWindow, self).__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.showMessage())

    # 定义自己设置的函数
    def showMessage(self):
        #弹出小窗口
        # QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")
        #打开一个新的窗口
        self.another.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())