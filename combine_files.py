from os import listdir
from pathlib import Path
from natsort import natsorted

input_dir = './input/'
output_dir = './output/'
filenames = natsorted([f for f in listdir(input_dir) if Path(input_dir + f).is_file()])


def write_header(begin, end, step):
    for text in texts[begin:end:step]:
        ouf.write(f'{text[0].strip()}\t')
    ouf.write('\n')


def write_lines(begin, end, step):
    for line in range(1, lines_number):
        for text in texts[begin:end:step]:
            ouf.write(f'{text[line].strip()}\t')
        ouf.write('\n')


texts = []
for filename in filenames:
    with open(input_dir + filename, 'r', encoding='utf-8') as inf:
        texts.append(inf.readlines())
lines_number = len(texts[0])

Path(output_dir).mkdir(parents=True, exist_ok=True)
with open(output_dir + 'field1.txt', 'w', encoding='utf-8') as ouf:
    write_header(0, len(texts), 2)
    write_lines(0, len(texts), 2)
with open(output_dir + 'field2.txt', 'w', encoding='utf-8') as ouf:
    write_header(1, len(texts), 2)
    write_lines(1, len(texts), 2)
