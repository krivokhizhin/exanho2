import json

from .ini_options import json_root_option

def read_actors_file(actors_file : str) -> list:
    with open(actors_file, 'r') as f:
        content = json.load(f)
        return content.get(json_root_option, [])

def write_actors_file(actor_configs : list, actors_file : str):
    content = {json_root_option : actor_configs}
    with open(actors_file, 'w') as f:
        json.dump(content, f)

def get_actor_config(actor_config : dict, indent=4):
    return json.dumps(actor_config, indent=indent)

def get_actor_configs(actor_configs : list, indent=4):
    content = {json_root_option : actor_configs}
    return json.dumps(content, indent=indent)

def get_actor_configs_from_file(actors_file : str, indent=4):
    with open(actors_file, 'r') as f:
        content = json.load(f)
        return json.dumps(content, indent=indent)