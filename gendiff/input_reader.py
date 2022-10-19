import json
import yaml
from gendiff import constants


def parse_file(file):
    opened_file = open(file)
    file_content = opened_file.read()
    filename_extension = file.split('.')[-1]
    return convert_data_to_dict(file_content, filename_extension)


def convert_data_to_dict(data, filename_extension):
    """Converts the input to python dictionary
    according to the filename extension"""
    match filename_extension:
        case constants.JSON:
            return json.loads(data)

        case constants.YAML | constants.YML:
            yaml_data = yaml.safe_load(data)
            return {} if yaml_data is None else yaml_data
