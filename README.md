ibatis2mybatis
==============

![mybatis](http://mybatis.github.io/images/mybatis-logo.png)

The tool is designed around an xslt transformation and some text replacements packaged in an ant task and tries to deliver a good starting point before the more complex work begins.

Usage:
Put Your old ibatis2 sqlmap files in the source folder and execute the ant build file.
The task converts Your sqlmap2 files to myBatis mappers in the destination folder and reports anything it cannot convert in the console.

Have fun and maybe You can post some improvements/bugfixes as this initial version is by no means perfect yet!

Greetings from Frankfurt/Germany

Peter Köhler

在本地安装好python环境
1.转换mapper文件：
修改conver_ibatis_to_mybatis.py里的文件路径，然后执行命令:python conver_ibatis_to_mybatis.py
2.更新相关的java文件：
修改conver_content.py里的文件路径，然后执行命令:python conver_content.py
