
import os
from orange import Path
from orange.sqlite import findone,execute
checksql='select path from ImportFile where path=? and mtime>=?'
replsql='insert or replace into ImportFile values(?,?)'

NT=os.name=='nt'

def _get_file(file):
    file=Path(file)
    path=str(file.absolute())
    if NT:
        path=path.lower()
    return path,file.mtime


def dumpcheck(file,func,*args,**kw):
    path=_get_file(file)
    record=findone(checksql,path)
    if not record:
        func(file,*args,**kw)
        execute(replsql,path)

async def adumpcheck(file,func,*args,**kw):
    path=_get_file(file)
    record=await findone(checksql,path)
    print('find ok')
    if not record:
        await func(file,*args,**kw)
        await execute(replsql,path)
    
    