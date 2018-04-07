# coding: shift-jis

#############################
# import
import re
import codecs

#############################
# テキスト変換情報解析
def analyze_text(converted_pdf_file):

	fp_in =  open(converted_pdf_file, 'r')
	for line in fp_in:
		
		# 局名をサーチ
		if re.match(r'"局名 ', line):
			print(line)
			broadcast=line.split('\t')
			print(broadcast)
		
		# 各局名毎の情報を収集
		
		# タブって出力される行を削除
		if re.match(r'"\D+"', line):
#			print(line)
			continue
		
		# 不要な"を削除
		line=line.replace('"', '')
		
		if re.search('\d{6}', line):
			print(line)
			broadinfo=line.split();
			print(broadinfo)
		
analyze_text('test.tsv')
#analyze_text('result.txt')

