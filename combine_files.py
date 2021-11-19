import sys
from os import listdir
from pathlib import Path
from typing import List
from natsort import natsorted


def combine_files(files: List, output_file: str):
    texts = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as inf:
            texts.append(inf.readlines())
    lines_number = max(len(text) for text in texts)
    with open(output_file, 'w', encoding='utf-8') as ouf:
        for line_number in range(lines_number):
            for text in texts:
                if line_number < len(text):
                    ouf.write(f'{text[line_number].strip()}\t')
                else:
                    ouf.write(f'\t')
            ouf.write('\n')


def main():

    choice = input('1: Combine all files\n2: Combine odd and even files separately\n3: Cancel\nEnter your choice: ')
    if choice not in ['1', '2']:
        print('Combine canceled')
        return

    input_dir = './detrended/'
    output_dir = './output/'
    files = natsorted([input_dir + f for f in listdir(input_dir) if Path(input_dir + f).is_file()])
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for f in Path(output_dir).glob('*.*'):
        f.unlink()
    if choice == '1':
        combine_files(files, output_dir + 'out.txt')
    else:
        files1 = files[::2]
        files2 = files[1::2]
        combine_files(files1, output_dir + 'out1.txt')
        combine_files(files2, output_dir + 'out2.txt')

    print(sys.version)
    print('Files combined successfully!')


if __name__ == '__main__':
    main()
