# 项目：工作平台
# 模块：安装模块
# 作者：黄涛
# License:GPL
# Email:huangtao.sh@icloud.com
# 创建：2018-02-13

from orange import setup
from coco.__version__ import version

__version__ = '0.1'

# 命令行程序入口
cscripts = [
    'coco=coco:main',
    'user=coco.users:Users.main'
]

setup(
    name='coco',
    author='huangtao',
    description='运营管理',
    entry_points={'console_scripts': cscripts, },
    version=version,
    package_data={'coco': ['sql/*.sql']},
)
