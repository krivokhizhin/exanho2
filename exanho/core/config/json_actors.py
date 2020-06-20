import json

from .ini_options import json_context_item, json_actors_item

def read_context_from_file(actors_file : str) -> dict:
    with open(actors_file, 'r') as f:
        content = json.load(f)
        return content.get(json_context_item, {})

def read_actors_from_file(actors_file : str) -> list:
    with open(actors_file, 'r') as f:
        content = json.load(f)
        return content.get(json_actors_item, [])

def write_actors_file(context:dict, actor_configs:list, actors_file:str):
    content = {
        json_context_item : context,
        json_actors_item : actor_configs
        }
    with open(actors_file, 'w') as f:
        json.dump(content, f)

def get_actor_config(actor_config : dict, indent=4):
    return json.dumps(actor_config, indent=indent)

def get_actor_configs(actor_configs : list, indent=4):
    content = {json_actors_item : actor_configs}
    return json.dumps(content, indent=indent)

def get_config_from_file(actors_file : str, indent=4):
    with open(actors_file, 'r') as f:
        content = json.load(f)
        return json.dumps(content, indent=indent)

def convert_config_to_dict(config: str) -> dict:
    return json.loads(config)