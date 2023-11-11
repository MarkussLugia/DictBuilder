def export(dict_list, proj, ver, title):
    fs = open('output/' + proj + '_BaiduInputAndroid_' +
                 ver + '.ini', mode='w+', encoding='utf_16_le')
    fs.write('\ufeff')
    fs.write('[' + title + ']' + '\n')
    for line in dict_list:
        fs.write(line[1] + '=0,' + line[0] + '\n')
    fs.close()
    