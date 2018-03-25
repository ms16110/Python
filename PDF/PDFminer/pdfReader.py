# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:36:08 2018

@author: Hirohito
"""

#import logging
#logging.basicConfig(level=logging.DEBUG, 
#                    format='%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')

#logging.debug('START')

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# ファイル名 
input_path = "chuukei_01hokkaido.pdf"
output_path = "result.txt"

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# 縦書き文字を横並びで出力する
#laparams.detect_vertical = True

# Set Text Converter(出力をｆｐ_outへ設定)
fp_out = open(output_path, 'wb')
device = TextConverter(rsrcmgr, fp_out, codec='utf-8', laparams=laparams)

# Set InterPreter
interpreter = PDFPageInterpreter(rsrcmgr, device)

# 処理するPDFを開く
fp_in = open(input_path, 'rb')

# InterPreter実行 maxpages：ページ指定（0は全ページ）
for page in PDFPage.get_pages(fp_in, pagenos=None, maxpages=0, password=None,caching=True, check_extractable=True):
    interpreter.process_page(page)
#for page in PDFPage.get_pages(fp_in):
#            interpreter.process_page(page)
 
# リソース開放 
fp_in.close()
fp_out.close()
device.close()

#logging.debug('END')
