#!/usr/bin/python3
"""Deploy archive!"""
from os.path import exists
from fabric.api import put, run, env

env.hosts = ['100.26.229.143', '100.26.246.95']


def do_deploy(archive_path):
    """Function distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        archive_file = file_name.split('.')[0]
        archive_folder_path = '/data/web_static/releases/'

        put(archive_path, '/tmp/')
        run(f'mkdir -p {archive_folder_path}{archive_file}')
        run(
            f'tar -xzf /tmp/{file_name} -c {archive_folder_path}{archive_file}'
        )
        run(f'rm -rf /tmp/{file_name}')
        run(f'mv {archive_folder_path}{archive_file}/web_static/* '
            f'{archive_folder_path}{archive_file}/')
        run(f'rm -rf {archive_folder_path}{archive_file}/web_static')
        run('rm -rf /data/web_static/current')
        run(
            f'ln -s {archive_folder_path}{archive_file}/'
            f' /data/web_static/current'
        )
        return True
    except Exception:
        return False
