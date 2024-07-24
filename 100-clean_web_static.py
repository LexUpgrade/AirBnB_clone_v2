#!/usr/bin/python3
"""
    Defines a Fabfile 'do_clean'.
"""

from fabric.api import local, run, env, lcd, cd

env.hosts = ["web-01.lexcraft.tech", "web-02.lexcraft.tech"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_clean(number=0):
    """Deletes out-of-date archives from both local and remote machine."""

    number = 1 if int(number) == 0 else int(number)

    with lcd("versions"):
        archives = local("ls -tr", capture=True).split()
        if len(archives) > number:
            archives_to_remove = archives[:-number]
            if archives_to_remove:
                local("rm -rf {}".format(" ".join(archives_to_remove)))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [f for f in archives if "web_static_" in f]
        if archives:
            archives_to_remove = archives[:-number]
            if archives_to_remove:
                run("rm -rf {}".format(" ".join(archives_to_remove)))
