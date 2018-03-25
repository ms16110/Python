# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 220, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblMyFunc = QtWidgets.QLabel(Dialog)
        self.lblMyFunc.setGeometry(QtCore.QRect(160, 80, 48, 16))
        self.lblMyFunc.setObjectName("lblMyFunc")
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.btnClose.setObjectName("btnClose")
        self.btnMyFunc = QtWidgets.QPushButton(Dialog)
        self.btnMyFunc.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.btnMyFunc.setObjectName("btnMyFunc")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.btnClose.clicked.connect(Dialog.close)
        self.btnMyFunc.clicked.connect(Dialog.MyFunc)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblMyFunc.setText(_translate("Dialog", "初期状態"))
        self.btnClose.setText(_translate("Dialog", "終了"))
        self.btnMyFunc.setText(_translate("Dialog", "MyFunc"))

