from json import dumps,loads
from orange.sqlite import executemany,find

GangWei='''R01:交易发起岗
R02:前台授权岗
R03:凭证管理岗
R04:分中心授权岗
R05:权限申请发起岗
R06:权限管理岗
R07:审查比对岗
R08:人工验印岗
R09:后台录入岗
R10:附加要素补录岗
R11:后台授权岗
R12:业务监测岗
R13:异常授权岗
R14:异常处理岗
R15:权限管理授权岗
R16:审查复核岗
R17:附加要素复核岗
R18:数据录入岗
R19:数据复核岗
R20:验票与保管岗
R21:审查岗
R22:信用卡审查岗
R41:放款受理人
R42:放款审核人
R43:放款核准人
R44:放款复核人
R45:业务审核岗'''

Columns=0,1,2,4,6,7,35,37,38,39,50,51,52,53,54,55,56,58,59
gw={}
for k in GangWei.split('\n'):
    a,b=k.split(':')
    gw[a]=b

class Users(object):
    @classmethod
    async def load(cls,file):
        sql=f'insert or replace into Users values ({",".join(["?"]*20)})'
        data=[]
        for row in file.iter_csv():
            d=[row[x].strip() for x in Columns]
            gg={}
            for i,name in enumerate(gw,8):
                v=row[i].strip()
                if v:
                    gg[name]=v
            d.insert(6,dumps(gg))
            data.append(d)
        await executemany(sql,data)
        print(f'共导入数据{len(data)}条')

    @classmethod
    def paicha(cls):
        print('排查用户表')
        
        sql='''select branch,id,name from Users where substr(status,1,1) 
        not in ("3","4") and rzlx="0" '''
        d=find(sql)
        if (d):
            print('-'*40)
            print('未使用指纹柜员排查')
            for r in d:
                print(*r)
            print(f'共查出柜员{len(d)}条记录')
            
        sql='''select branch,id,name,count(name) as c,zjzl,zjhm from Users where substr(status,1,1) 
        not in ("3","4") 
        group by branch,zjzl,zjhm,name
        having c>1 
        order by branch,id
        '''
        d=find(sql)
        if (d):
            print('-'*40)
            print('同机构开立多个柜员排查')
            for r in d:
                print(*r)
            print(f'共查出柜员{len(d)}条记录')
            

            
        