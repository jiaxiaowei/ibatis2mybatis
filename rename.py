#把ibatis转mybatis后的文件自动重命名

import os

path = '/Users/jiaxiaowei/Downloads/ibatis2mybatis-master/destination'
for file in os.listdir(path):
    newName = file.capitalize() #首字母大写
    newName = newName.replace('.mysql.ibatis.xml','Mapper.mysql.xml')
    os.rename(os.path.join(path,file),os.path.join(path,newName))
