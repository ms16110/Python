# coding: shift-jis

#############################
# import
import re
import codecs

#############################
# �e�L�X�g�ϊ������
def analyze_text(converted_pdf_file):

	fp_in =  open(converted_pdf_file, 'r')
	for line in fp_in:
		
		# �ǖ����T�[�`
		if re.match(r'"�ǖ� ', line):
			print(line)
			broadcast=line.split('\t')
			print(broadcast)
		
		# �e�ǖ����̏������W
		
		# �^�u���ďo�͂����s���폜
		if re.match(r'"\D+"', line):
#			print(line)
			continue
		
		# �s�v��"���폜
		line=line.replace('"', '')
		
		if re.search('\d{6}', line):
			print(line)
			broadinfo=line.split();
			print(broadinfo)
		
analyze_text('test.tsv')
#analyze_text('result.txt')

