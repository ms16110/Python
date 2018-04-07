# coding: utf-8

#############################
# import
import csv

#############################
# テキスト変換情報解析
def csvFileWrite(output_csvfile, tlist):
	
	fp_out = open(output_csvfile, 'w')

	# CSV Writer
	writer = csv.writer(fp_out, lineterminator='\n')

	for item in tlist:
		writer.writerow(item)

	fp_out.close()

