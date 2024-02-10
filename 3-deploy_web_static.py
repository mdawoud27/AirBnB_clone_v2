#!/usr/bin/python3
"""Full deployment"""
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists

env.hosts = ['100.26.229.143', '100.26.246.95']


def do_pack():
    """Function that generates a .tgz archive
    from the content of web_static folder of AirBnB repo
    """
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f'web_static_{current_time}.tgz'
    local("mkdir -p versions")
    create_file = local(f'tar -cvzf versions/{archive_name} web_static')
    if create_file is not None:
        return archive_name
    else:
        return None


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


def deploy():
    """Function that creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path=archive_path)
