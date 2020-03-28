import json

from .ini_options import json_root_option

def read_actors_file(actors_file : str) -> list:
    with open(actors_file, 'r') as f:
        content = json.load(f)
        return content.get(json_root_option, [])

def write_actors_file(actors_file : str, actor_configs : list):
    content = {json_root_option : actor_configs}
    with open(actors_file, 'w') as f:
        json.dump(content, f)