import json
import yaml


def parsing_file(file):
    """Detects filename extension and returns
    converted opened file"""
    filename_extension = file.split('.')[-1]
    match filename_extension:
        case 'json':
            return json.load(open(file))
        case 'yaml' | 'yml':
            yaml_data = yaml.safe_load((open(file)))
            return {} if yaml_data is None else yaml_data
