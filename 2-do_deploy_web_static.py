#!/usr/bin/python3
"""
    FabFile to generates a .tgz archive from the contents of web_static.
"""
from os.path import exists
from fabric.api import *


env.hosts = ["web-01.lexcraft.tech", "web-02.lexcraft.tech"]
env.ubuntu = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """
        Distributes an archive to my web servers.
    """

    if not exists(archive_path):
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
