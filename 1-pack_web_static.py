#!/usr/bin/python3
"""
    FabFile to generates a .tgz archive from the contents of web_static.
"""

import os
from fabric.api import *
from datetime import datetime


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
