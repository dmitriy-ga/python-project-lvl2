import json
import yaml


def parsing_file(file):
    return parsing_data(*open_file(file))


def open_file(file):
    """Returns inputted file and filename extension of it"""
    return open(file), file.split('.')[-1]


def parsing_data(data, filename_extension):
    """Converts the input to python dictionary
    according to the filename extension"""
    match filename_extension:
        case 'json':
            return json.load(data)
        case 'yaml' | 'yml':
            yaml_data = yaml.safe_load(data)
            return {} if yaml_data is None else yaml_data
