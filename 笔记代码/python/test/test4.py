#coding:utf -8
import re,os
File_Path = "./"

def alter(file,old_str,new_str):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    with open(file, "r+") as f1,open("%s.txt" % file, "w") as f2:
        for x in f1:
            line = x#.decode('gb2312').encode('utf-8')
            if old_str in line:
                line = line.replace(old_str, new_str)
                print line
            f2.write(line)
    f2.close()
    os.remove(file)
    os.rename("%s.txt" % file, file)

def run(File_Path):
  os.chdir(File_Path)#切换到目标文件所在目录
  for file_name in os.listdir(os.getcwd()):
      if os.path.splitext(file_name)[1] == '.txt':
        # alter(file_name,  "。”，"   ,"。”")

if __name__ == '__main__':
  run(File_Path)