import sys
from os import listdir
from pathlib import Path
from typing import List
from natsort import natsorted


def combine_files(filenames: List, output_filename: str):
    texts = []
    for filename in filenames:
        with open(input_dir + filename, 'r', encoding='utf-8') as inf:
            texts.append(inf.readlines())
    lines_number = len(texts[0])
    with open(output_dir + output_filename, 'w', encoding='utf-8') as ouf:
        for line in range(lines_number):
            for text in texts:
                ouf.write(f'{text[line].strip()}\t')
            ouf.write('\n')


input_dir = './detrended/'
output_dir = './output/'
filenames = natsorted([f for f in listdir(input_dir) if Path(input_dir + f).is_file()])
filenames1 = filenames[::2]
filenames2 = filenames[1::2]
Path(output_dir).mkdir(parents=True, exist_ok=True)
combine_files(filenames1, 'field1.txt')
combine_files(filenames2, 'field2.txt')
print(sys.version)
print('Files combine done successfully!')
