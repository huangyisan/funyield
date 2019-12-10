# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mywindow(object):
    def setupUi(self, mywindow):
        mywindow.setObjectName("mywindow")
        mywindow.resize(227, 306)
        self.centralwidget = QtWidgets.QWidget(mywindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.testbutton = QtWidgets.QPushButton(self.centralwidget)
        self.testbutton.setObjectName("testbutton")
        self.verticalLayout.addWidget(self.testbutton)
        mywindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mywindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 227, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        mywindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mywindow)
        self.statusbar.setObjectName("statusbar")
        mywindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(mywindow)
        QtCore.QMetaObject.connectSlotsByName(mywindow)

    def retranslateUi(self, mywindow):
        _translate = QtCore.QCoreApplication.translate
        mywindow.setWindowTitle(_translate("mywindow", "MainWindow"))
        self.label.setText(_translate("mywindow", "TextLabel"))
        self.testbutton.setText(_translate("mywindow", "testbutton"))
        self.menufile.setTitle(_translate("mywindow", "file"))

a = Ui_mywindow()
a.setupUi()