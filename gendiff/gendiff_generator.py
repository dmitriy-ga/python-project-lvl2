from collections import OrderedDict
from gendiff.input_reader import parsing_file
from gendiff.output_formatters import style_formatting


def generate_diff(file1, file2, style='stylish'):
    def is_dict(item):
        return isinstance(item, dict)

    def get_diffs(dict1, dict2):
        # Dictionary of untouched items
        stays = {f'  {key}': value
                 for key, value in dict1.items()
                 if key in dict2
                 and value == dict2.get(key)
                 }

        # Dictionary of deleted items
        deletes = {f'- {key}': value
                   for key, value in dict1.items()
                   if key not in dict2
                   or all((key in dict2,
                           value != dict2.get(key),
                           not is_dict(value))
                          )
                   or is_dict(value) ^ is_dict(dict2.get(key))
                   }

        # Dictionary of added items
        adds = {f'+ {key}': value
                for key, value in dict2.items()
                if key not in dict1
                or all((key in dict1,
                        value != dict1.get(key),
                        not is_dict(value))
                       )
                or is_dict(value) ^ is_dict(dict1.get(key))
                }

        # Dictionary of changed nested dictionaries
        modded_dicts = {f'{key}': get_diffs(value, dict2.get(key))
                        for key, value in dict1.items()
                        if all((is_dict(value),
                                is_dict(dict2.get(key)),
                                key in dict2,
                                value != dict2.get(key))
                               )
                        }

        # Building and sorting python dictionary
        result_diffs = OrderedDict(stays | deletes | adds | modded_dicts)
        for name in sorted(result_diffs, key=lambda x: x.split()[-1]):
            result_diffs.move_to_end(name)
        return result_diffs

    # Loading files to dictionaries
    dict_old = parsing_file(file1)
    dict_new = parsing_file(file2)

    diffs = get_diffs(dict_old, dict_new)

    # Formatting and returning diffs
    return style_formatting(diffs, style)
