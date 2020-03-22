import os
import re
import subprocess

from inspect import currentframe, getframeinfo
from pathlib import Path


    
template = 'exanho-service.ini'
service_name = template.split('.')[0] + '.service'
template_dir = 'etc'
service_dir = '/etc/systemd/system'
venv_dir = '/venv/bin'

fullpath = service_dir + '/' + service_name
temp_fullpath = '/tmp/' + service_name

def install():
    filename = getframeinfo(currentframe()).filename
    resolver = Path(filename).resolve()
    parent, fullpath_venv = resolver.parents[0], resolver.parents[2]
    print(parent, fullpath_venv)
    
    content = ''
    with open('{}/{}/{}'.format(parent, template_dir, template), 'r') as t:
        content = t.read()
    
    print(content)
    content = re.sub(r'\{VENV_DIR\}', '{}{}/'.format(fullpath_venv, venv_dir), content)
    content = re.sub(r'\{APP_DIR\}', '{}/'.format(fullpath_venv), content)
    print(content)
    
    with open(temp_fullpath, 'w') as unit_file:
        unit_file.write(content)
        
    subprocess.call(['sudo', 'mv', temp_fullpath, service_dir])
    subprocess.call(['sudo', 'systemctl', 'daemon-reload'])
    subprocess.call(['sudo', 'systemctl', 'enable', service_name])
    subprocess.call(['sudo', 'systemctl', 'start', service_name])

def uninstall():
    if not(os.path.exists(fullpath)) or not(os.path.isfile(fullpath)):
        print('Service "{}" was not found in the system'.format(service_name))
        return
    
    is_active = _subprocess_check_output(['sudo', 'systemctl', 'is-active', service_name])
    if is_active == 'active':
        subprocess.call(['sudo', 'systemctl', 'stop', service_name])
        
    is_enabled = _subprocess_check_output(['sudo', 'systemctl', 'is-enabled', service_name])
    if is_enabled == 'enabled':
        subprocess.call(['sudo', 'systemctl', 'disable', service_name])
    
    subprocess.call(['sudo', 'rm', fullpath])
    subprocess.call(['sudo', 'systemctl', 'daemon-reload'])

def _subprocess_check_output(args):
    out = ''
    try:
        out = subprocess.check_output(args)
    except subprocess.CalledProcessError as e:
        out = e.output
                
    return out.decode('utf-8').rstrip()