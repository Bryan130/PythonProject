#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time


def del_files(del_path, del_file_format):
    del_file_list = []
    for root , dirs, files in os.walk(del_path):
        for name in files:
            for file_format in del_file_format:
                if name.endswith(file_format):
                    now = time.strftime("%Y-%m-%d %H:%M:%S")
                    os.remove(os.path.join(root, name))
                    del_file = os.path.join(root, name)
                    del_file = "[ " + now + " ]" + " [ DELETE ]  " + del_file
                    del_file_list.append(del_file)
    return del_file_list


def write_result(filename, del_file_list):
    fopen = open(filename, 'a')
    for temp in del_file_list:
        fopen.write(temp+'\n')
    fopen.write('\n')
    fopen.close()


if __name__ == "__main__":
    # 删除文件的目标目录，支持绝对路径和相对路径，建议用绝对路径
    del_path = 'F:/Z_other/PythonProject/py2/delFile/testFile'  # 这是绝对路径
    # del_path = './testFile'   # 这是相对路径
    # 删除文件的格式，以什么结尾。   例如： ".txt",将会删除目标目录下所有以.txt结尾的文件
    del_file_format = ['.rvt', '.txt']
    # 删除的文件名写入的文件, 支持绝对路径和相对路径，建议用绝对路径
    filename = 'F:/Z_other/PythonProject/py2/delFile/del_file.log'    # 这是绝对路径
    # filename = './del_file_log.log'   # 这是相对路径
    # 删除文件
    del_file_list = del_files(del_path, del_file_format)
    # 记录删除的文件
    write_result(filename, del_file_list)
    print "Delete the files successfully!"
    print "Check the deletion details path: " + filename
