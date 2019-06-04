import os

for file in os.listdir('./source'):
    os.remove(os.path.join(os.path.join(os.getcwd(),'source'),file))

rootPath = '/Users/jiaxiaowei/work/svn_kuotu/jii_trunk/istore'
#递归遍历目录
for root, dirs, files in os.walk(rootPath):
    for file in files:
        #打印命名不正确的xml文件
        if(file.endswith('.ibatis.xml')
                and not (file.endswith('mysql.ibatis.xml')
                         or file.endswith('oracle.ibatis.xml')
                         or file.endswith('mssql.ibatis.xml'))):
            print(os.path.join(root,file))
        if(file.endswith('mysql.ibatis.xml')):
            currentPath = os.path.join(root,file)
            sourcePath = os.path.join(os.path.join(os.getcwd(),'source'),file)
            open(sourcePath, "wb").write(open(currentPath, "rb").read())
            try:
                os.system('ant')
                os.remove(sourcePath)

                # 把ibatis转mybatis后的文件自动重命名
                newName = file[0].capitalize() + file[1:len(file)] # capitalize()会把首字母大写，其他字母会全部变为小写
                newName = newName.replace('.mysql.ibatis.xml', 'Mapper.mysql.xml')

                newPath = os.path.join(os.path.join(os.getcwd(), 'destination'), newName)
                oldPath = os.path.join(os.path.join(os.getcwd(), 'destination'), file)
                os.rename(oldPath, newPath)

                # 转换好的文件复制回原目录
                print("success: {0}".format(os.path.join(root, newName)))

                open(os.path.join(root,newName), "wb").write(open(newPath, "rb").read())
                os.remove(newPath)
            except:
                print('ant error: {0}'.format(sourcePath))
