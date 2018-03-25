# coding: utf-8

import PyPDF2
import codecs

pdf_file_obj = open('test.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
page_obj = pdf_reader.getPage(0)

text=page_obj.extractText()

fp_wr = codecs.open("result.txt", 'w', 'utf-8')
fp_wr.write(text)
fp_wr.close()

