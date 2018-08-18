# 项目：运营管理模块
# 模块：主查获块
# 作者：黄涛
# License:GPL
# Email:huangtao.sh@icloud.com
# 创建：2018-08-18 08:32

from orange import Path,arg
from orange.sqlite import db_config,connect,executefile,execute
from .checkfile import dumpcheck,adumpcheck
from .users import Users 

db_config('coco')

@arg('-i','--init',action='store_true',help='初始化数据库表')
@arg('-t','--test',action='store_true',help='测试')
def main(init=False,test=False):
    if init:
        with connect():
            executefile(__package__,'sql/createtable.sql')
            print('批量建立数据库表成功')
    if test:
        with connect():
            Users.paicha()

