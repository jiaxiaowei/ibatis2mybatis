#把Dao文件重命名为Mapper文件

import os
import fnmatch

#项目根路径，会遍历处理下面的所有字目录文件
rootPaths = ['/Users/jiaxiaowei/work/svn_kuotu/kuotu_trunk/',
            '/Users/jiaxiaowei/work/SVN_xian/MDS/java_src/trunk/java/']

# 文件内容全局替换
# src 表示要被替换的内容
# dest 表示 替换后的内容
def file_switch(filePath, src, dest):
    with open(filePath, "r", encoding="utf-8") as f:
        # readlines以列表的形式将文件读出
        lines = f.readlines()

    with open(filePath, "w", encoding="utf-8") as f_w:
        for line in lines:
            if src in line:
                line = line.replace(src, dest)
            f_w.write(line)

def change_dao_file_name(file):
    # 修改原Dao文件
    if (file.endswith('Dao.java')):
        newName = file.replace('Dao.java', 'Mapper.java')
        newPath = os.path.join(root, newName)
        oldPath = os.path.join(root, file)
        os.rename(oldPath, newPath)
        file_switch(newPath, 'Dao', 'Mapper')

# 修改所有import *Dao
def change_import(file):
    if (file.endswith('java')):
        # 先将文件读取到内存中
        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 再写的方式打开文件
        with open(os.path.join(root, file), "w", encoding="utf-8") as f_w:
            for line in lines:
                if (fnmatch.fnmatch(line, "import*Dao;\n") or fnmatch.fnmatch(line, "Dao.")):
                    line = line.replace('Dao', 'Mapper')
                if (fnmatch.fnmatch(line, "*Dao.*")):
                    line = line.replace('Dao', 'Mapper')
                if (fnmatch.fnmatch(line, "*敖建*")):
                    line = line.replace('敖建', '')
                f_w.write(line)

#修改autiwired行的dao为mapper
def change_autowired_line(file):
    if (file.endswith('java')):
        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(os.path.join(root, file), "w", encoding="utf-8") as f_w:
            hit = False;#是否到了要处理的行
            for line in lines:
                if (hit):
                    hit = False
                if (fnmatch.fnmatch(line, "*@Autowired*")):
                    hit = True
                if (fnmatch.fnmatch(line, "*Dao*Dao*")):
                    line = line.replace('Dao', 'Mapper')
                    if (not line.startswith("private")):
                        line = "    private "+line

                f_w.write(line)

#递归遍历目录,重命名文件
for rootPath in rootPaths:
    for root, dirs, files in os.walk(rootPath):
        for file in files:
            change_dao_file_name(file)

#因为上面已经改了文件名，所以重新遍历一次文件来修改文件内容，否则会报文件找不到
for rootPath in rootPaths:
    for root, dirs, files in os.walk(rootPath):
        for file in files:
            change_import(file)
            change_autowired_line(file)