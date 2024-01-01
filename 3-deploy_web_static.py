#!/usr/bin/python3
""" Fabric script to create and distribute an archive to web servers """
from fabric.api import task, execute
from os.path import exists

@task
def deploy():
    """ Deploy the archive to web servers """

    # Call the do_pack() function and store the path of the created archive
    archive_path = execute(do_pack)

    # Return False if no archive has been created
    if not archive_path or not archive_path['<IP web-01>']:
        return False

    # Call the do_deploy(archive_path) function
    result = execute(do_deploy, archive_path=archive_path['<IP web-01>'])

    # Return the return value of do_deploy
    return result['<IP web-01>']

# Rest of the script (do_pack, do_deploy, etc.) remains unchanged
