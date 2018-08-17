-- 导入文件清单
create table if not exists ImportFile(
    path  text primary key,       -- 文件目录
    mtime int                     -- 修改时间
);

-- 柜员表 
create table if not exists Users(
    id       text primary key,    -- 柜员号
    name     text not null,       -- 姓名
    tel      text,                -- 电话
    rank     text,                -- 柜员级别
    branch   text,                -- 机构
    userid   text,                -- 员工号
    gangwei  text,                -- 岗位
    zxjyz    text,                -- 可执行交易组
    zzxe     text,                -- 转账限额
    xjxe     text,                -- 现金限额
    rzlx     text,                -- 认证类型
    status   text,                -- 状态
    pbjy     text,                -- 屏蔽交易
    gwxz     text,                -- 岗位性质
    qyrq     text,                -- 启用日期
    zzrq     text,                -- 终止日期
    czbz     text,                -- 操作币种
    fqjyz    text,                -- 发起交易组
    zjzl     text,                -- 证件种类
    zjhm     text                 -- 证件号码
)