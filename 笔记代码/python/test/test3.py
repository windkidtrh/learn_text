#coding:utf -8
import os
def alter(file,old_str,new_str):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    with open(file, "r+") as f1,open("%s.doc" % file, "w") as f2:
        for x in f1:
            line = x.decode('utf-16').encode('utf-8')
            if old_str in line:
                line = line.replace(old_str, new_str)
                print line
            f2.write(line)
   	f2.close()
    os.remove(file)
    os.rename("%s.doc" % file, file)

File_path='1.doc'

alter(File_path,  "。”，"   ,"。”")