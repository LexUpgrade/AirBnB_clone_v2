#!/usr/bin/python3
"""
    Defines FabFile functions:
        - do_pack.
        - do_deploy.
        - deploy.
"""

import os
from fabric.api import env, put, run, local
from datetime import datetime

env.hosts = ["web-01.lexcraft.tech", "web-02.lexcraft.tech"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_pack():
    """
        Creates a tar gzipped archive of the directory web_static.
    """

    if os.path.isdir("versions") is False:
        local("mkdir -p versions")
    tgz_name = "versions/web_static_{}.tgz".\
        format(datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static/*".format(tgz_name))
    if result.succeeded:
        return tgz_name
    else:
        return None


def do_deploy(archive_path):
    """
        Distributes an archive to my web servers.
    """

    if not os.path.exists(archive_path):
        return False

    folder = archive_path.split('.')[0].split('/')[-1]
    folder = "/data/web_static/releases/" + folder
    tmp = "/tmp/" + archive_path.split('/')[-1]
    try:
        put(local_path=archive_path, remote_path=tmp)
        run("mkdir -p {}/".format(folder))
        run("tar -xzf {} -C {}/".format(tmp, folder))
        run("rm -rf {}".format(tmp))
        run("rm -rf /data/web_static/current")
        run("mv {0}/web_static/* {0}/".format(folder))
        run("rm -rf {}/web_static".format(folder))
        run("ln -sf {} /data/web_static/current".format(folder))
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to my two servers."""

    archive_path = do_pack()
    if archive_path is not None:
        return (do_deploy(archive_path))
    return False
