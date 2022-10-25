import json
import yaml

JSON = 'json'
YAML = 'yaml'
YML = 'yml'


def parse_file(file):
    opened_file = open(file)
    file_content = opened_file.read()
    filename_extension = file.split('.')[-1]
    return convert_data_to_dict(file_content, filename_extension)


def convert_data_to_dict(data, filename_extension):
    """Converts the input to python dictionary
    according to the filename extension"""
    if filename_extension == JSON:
        json_data = json.loads(data)
        return {} if json_data is None else json_data

    elif filename_extension in (YAML, YML):
        yaml_data = yaml.safe_load(data)
        return {} if yaml_data is None else yaml_data

    else:
        raise ValueError('Supported file format not found')
