# 项目：运营管理模块
# 模块：重复文件导入检查模块
# 作者：黄涛
# License:GPL
# Email:huangtao.sh@icloud.com
# 创建：2018-08-18 08:28

import os
from orange import Path
from orange.sqlite import findone, execute

checksql = 'select path from ImportFile where path=? and mtime>=?'
replsql = 'insert or replace into ImportFile values(?,?)'
NT = os.name == 'nt'    # 是否为 Windows 操作系统


def _get_file(file):    # 获取文件名及修改时间
    file = Path(file)
    path = str(file.absolute())
    if NT:       # Windows 操作系统时，把文件名转换成小写
        path = path.lower()
    return path, file.mtime


def dumpcheck(file, func, *args, **kw):
    path = _get_file(file)
    record = findone(checksql, path)
    if not record:
        func(file, *args, **kw)
        execute(replsql, path)


async def adumpcheck(file, func, *args, **kw):
    path = _get_file(file)
    record = await findone(checksql, path)
    print('find ok')
    if not record:
        await func(file, *args, **kw)
        await execute(replsql, path)
