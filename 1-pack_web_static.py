#!/usr/bin/python3
""" Fabric script to generate a .tgz archive from web_static folder """
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """ Creates a .tgz archive from web_static folder """

    # Create versions folder if it doesn't exist
    local("mkdir -p versions")

    # Create archive name
    archive_name = "web_static_{}.tgz".format(
        datetime.utcnow().strftime("%Y%m%d%H%M%S")
    )

    # Create the .tgz archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return os.path.abspath("versions/{}".format(archive_name))
    else:
        return None
