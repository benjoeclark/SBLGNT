#!/usr/bin/env python3
import os

def get_chapter_and_verse(line):
    line = line.replace('\t', ' ')
    return line.split(' ')[1]

def get_text(line):
    return line.split('\t')[-1]

def get_filename(text_filename):
    filename = None
    with open(text_filename) as f:
        filename = f.readline().strip()
    return filename

def make_obsidian_file(text, directory):
    filename = get_filename(text)
    with open(text) as f_text:
        f_text.readline() # throw away the filename
        with open(os.path.join(directory, filename + '.md'), 'w') as f_md:
            for line in f_text:
                line = line.strip()
                f_md.write(get_text(line) + '\n')
                f_md.write(' ^' + get_chapter_and_verse(line) + '\n')
            

if __name__ == '__main__':
    data_dir = 'data/sblgnt/text'
    target_dir = 'SBLGNT'
    for text_filename in os.listdir(data_dir):
        if '.txt' in text_filename:
            make_obsidian_file(text=os.path.join(data_dir, text_filename), directory=target_dir)
