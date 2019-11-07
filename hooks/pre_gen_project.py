# -*- coding: utf-8 -*-
import os


tmpl = """UID={uid}
GID={gid}
JUPYTER_PORT={{ cookiecutter.jupyter_port }}
TFBOARD_PORT={{ cookiecutter.tensorboard_port }}
"""

gid = os.getgid()
uid = os.getuid()

with open('./.env', 'w') as f:
    f.write(tmpl.format(gid=gid, uid=uid))
