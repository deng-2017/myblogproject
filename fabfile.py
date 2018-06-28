# -*- coding: utf-8 -*-

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/deng-2017/myblog.git"

env.user = 'deng'
env.password = '19911130dbyDBY'

# 填写你自己的主机对应的域名
env.hosts = ['dcookies.xyz']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/deng/sites/dcookies.xyz/myblog'

    sudo('cd %s && git pull' %source_folder)
    sudo("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python manage.py collectstatic --noinput &&
        ../env/bin/python manage.py makemigrations &&
        ../env/bin/python manage.py migrate
        """.format(source_folder)) 
    sudo('systemctl restart dcookies.xyz')
    sudo('nginx -s reload')

