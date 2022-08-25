from collections import OrderedDict
import json
import yaml


def generate_diff(file1, file2):

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

    def get_diffs(dict1, dict2):
        # Dictionary of untouched items
        stays = {f'  {key}': value
                 for key, value in dict1.items()
                 if value == dict2.get(key)}

        # Dictionary of deleted items
        deletes = {f'- {key}': value
                   for key, value in dict1.items()
                   if key not in dict2.keys()
                   or all((key in dict2.keys(), value != dict2.get(key)))}

        # Dictionary of added items
        adds = {f'+ {key}': value
                for key, value in dict2.items()
                if key not in dict1.keys()
                or all((key in dict1.keys(), value != dict1.get(key)))}

        # Building and sorting python dictionary
        result_diffs = OrderedDict(stays | deletes | adds)
        for name in sorted(result_diffs, key=lambda x: x.split()[-1]):
            result_diffs.move_to_end(name)
        return result_diffs

    # Loading files to dictionaries
    dict_old = parsing_file(file1)
    dict_new = parsing_file(file2)

    diffs = get_diffs(dict_old, dict_new)

    # JSON output with diffs
    new_json = json.dumps(diffs, indent=2)
    new_json = new_json.replace('"', '')
    print(new_json)
    return new_json
