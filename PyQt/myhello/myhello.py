# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore as Qc, QtGui as Qg, QtWidgets as Qw    #�i�⑫1�j
from PyQt5.QtCore import Qt

import hello                                #�f�U�C�i�[�ō������ʂ��C���|�[�g����

class MyForm(Qw.QMainWindow):               #MyForm�Ƃ������O��QMainWindow�̃T�u�N���X�쐬

    def __init__(self, parent=None):        #�N���X�̏�����

        super().__init__(parent)            #��ʃN���X�̏��������[�`�����Ăяo���i�⑫2�j
        self.ui = hello.Ui_MainWindow()     #��قǍ����hello.py�̒��ɂ���N���X��
        self.ui.setupUi(self)               #���̃R�}���h�����s����

if __name__ == '__main__':

    app = Qw.QApplication(sys.argv)         #�p�����[�^�͐������̓R�}���h���C��������^����
    wmain = MyForm()                        #MyForm�̃C���X�^���X�������
    wmain.show()                            #�\������
    sys.exit(app.exec())                    #��������ďI���R�[�h��n���Ĕ�����̂���V


