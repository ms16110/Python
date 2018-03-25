# coding: utf-8

#############################
# import lib
import os

#############################
# import module
import pdfReader as pR
import txtAnalyze as tA


#############################
# グローバル

targetdir='broadcast'


#############################
# 処理
targetdir=os.path.join(os.getcwd(),targetdir)

# ターゲットのファイルを順次処理
for filename in os.listdir(targetdir):
	if filename.endswith('.pdf'):
		# PDFファイル名
		targetFile=os.path.join(targetdir, filename)
		print(targetFile)
		# 変換後のTXTファイル
		tempFile=targetFile.replace('.pdf', '.txt')
		print(tempFile)
		
		#########################
		# PDFをTXTに変換
		pR.pdf2Text(targetFile, tempFile)

		# 変換後のEXCEL名
		excelFile=tempFile.replace('.txt', '.xlsx')

		#########################
		# TXTをEXCELに変換
		tA.txt2Excel(tempFile, excelFile)

