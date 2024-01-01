#!/usr/bin/python3
""" Fabric script to distribute an archive to web servers """
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """ Deploys an archive to web servers """

    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>/
        filename_no_ext = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(filename_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_path.split('/')[-1], filename_no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_path.split('/')[-1]))

        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
            filename_no_ext))

        return True

    except Exception as e:
        return False
