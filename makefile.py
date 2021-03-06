import os
import zipfile

def outqq(list):
    write = open('output/' + proj + '_QQInputAndroid_' + ver + '.txt', mode='w+', encoding='utf_16_le')
    write.write('\ufeff')
    for line in list:
        parts = line.split(spliter)
        write.write(parts[0] + '=1,' + parts[1])
    write.close()

def outbaidu(list):
    write = open('output/' + proj + '_BaiduInputAndroid_' + ver + '.ini', mode='w+', encoding='utf_16_le')
    write.write('\ufeff')
    write.write('[' + title + ']' + '\n')
    for line in list:
        parts = line.split(spliter)
        write.write(parts[0] + '=0,' + parts[1])
    write.close()

def outsogou(list):
    write = open('output/' + proj + '_SogouPC_' + ver + '.txt', mode='w+', encoding='UTF-8')
    for line in list:
        parts = line.split(spliter)
        write.write(parts[0] + ',1=' + parts[1])
    write.close()

def outgb(list):
    write = open('dictionary.txt', mode='w+', encoding='UTF-8')
    write.write('# Gboard Dictionary version:1' + '\n')
    for line in list:
        parts = line.split(spliter)
        write.write(parts[0] + '	' + parts[1].strip('\n') + '	zh-CN	\n')
    write.close()
    archive = zipfile.ZipFile('output/' + proj + '_GboardAndroid_' + ver + '.zip', 'w')
    archive.write('dictionary.txt', compress_type=zipfile.ZIP_DEFLATED)
    archive.close()
    os.remove('dictionary.txt')

ver = input('INPUT VERSION NAME:')
conf = open('buildconfig.txt', encoding='UTF-8')
source = conf.readline().strip('\n')
spliter = conf.readline().strip('\n')
proj = conf.readline().strip('\n')
title = conf.readline().strip('\n')
conf.close()
src = open(source, encoding='UTF-8')
srclines = src.readlines()
src.close()
if not os.path.isdir('output'):
    os.mkdir('output')
outqq(srclines)
outbaidu(srclines)
outsogou(srclines)
outgb(srclines)
