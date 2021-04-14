import base64
import json

def form(obj, *obj_types) -> str:
    content = convert_obj_to_json_str(obj, *obj_types)
    return _convert_content_to_base64(content)

def deform(content:str, obj_type):
    json_str = _convert_base64_to_content(content)
    return convert_json_str_to_obj(json_str, obj_type)

def convert_obj_to_json_str(obj, *obj_types) -> str:
    result = _prepare_dict_to_dict(obj.__dict__, *obj_types)
    return json.dumps(result)

def convert_json_str_to_obj(json_str:str, obj_type):
    return json.loads(json_str, object_hook=obj_type)

def _prepare_dict_to_dict(dict_obj:dict, *obj_types) -> dict:
    result = dict()
    
    for key, value in dict_obj.items():
        if value or value==0:
            if isinstance(value, obj_types):
                result[key] = _prepare_dict_to_dict(value.__dict__, *obj_types)
            elif isinstance(value, dict):
                result[key] = _prepare_dict_to_dict(value, *obj_types)
            elif isinstance(value, list):
                result[key] = _prepare_list_to_dict(value, *obj_types)
            else:
                result[key] = value

    return result

def _prepare_list_to_dict(list_obj:list, *obj_types) -> list:
    result = list()

    for item in list_obj:
        if item or item == 0:
            if isinstance(item, obj_types):
                result.append(_prepare_dict_to_dict(item.__dict__, *obj_types))
            elif isinstance(item, dict):
                result.append(_prepare_dict_to_dict(item, *obj_types))
            elif isinstance(item, list):
                result.append(_prepare_list_to_dict(item))
            else:
                result.append(item)

    return result

def _convert_content_to_base64(content:str) -> str:
    base64_bytes = content.encode('ascii')
    content_bytes = base64.b64encode(base64_bytes)
    return content_bytes.decode('ascii')

def _convert_base64_to_content(content:str) -> str:
    base64_bytes = content.encode('ascii')
    content_bytes = base64.b64decode(base64_bytes)
    return content_bytes.decode('ascii')