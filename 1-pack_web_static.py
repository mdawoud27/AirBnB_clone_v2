#!/usr/bin/python3
""" Compress before sending"""
from fabric.api import local
from datetime import datetime


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
