#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """def do_pack"""
    local("mkdir -p versions")
    fecha = datetime.now().strftime("%Y%M%d%H%M%S")
    name = "version/web_static_{}.tgz".format(fecha)
    try:
        local("tar -cvzf {} web_static/".format(name))
        return "web_static/{}".format(name)
    except Exception:
        return None
