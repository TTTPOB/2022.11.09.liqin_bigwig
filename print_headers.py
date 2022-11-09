import pyBigWig as pyw
import sys

input_file = sys.argv[1]

bw = pyw.open(input_file)
headers = bw.chroms()
print(input_file)
print(headers)