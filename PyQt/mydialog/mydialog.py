# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore as Qc, QtGui as Qg, QtWidgets as Qw    #（補足1）
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

import dialog                                #デザイナーで作った画面をインポートする

class MyDialog(QDialog):

    def __init__(self, parent=None):         #クラスの初期化
        super(MyDialog, self).__init__(parent)
        self.ui = dialog.Ui_Dialog()         #先ほど作ったhello.pyの中にあるクラスの
        self.ui.setupUi(self)                #このコマンドを実行する
    def MyFunc(self):
        self.ui.lblMyFunc.setText('MyFunc押下')


if __name__ == '__main__':

    app = Qw.QApplication(sys.argv)          #パラメータは正しくはコマンドライン引数を与える
    dialog = MyDialog()                      #MyFormのインスタンスを作って
    dialog.show()                            #表示する
    sys.exit(dialog.exec_())                    #こうやって終了コードを渡して抜けるのが礼儀


