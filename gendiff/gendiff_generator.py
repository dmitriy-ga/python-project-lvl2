from collections import OrderedDict
from gendiff.input_reader import parsing_file
from gendiff.formatters.output_formatters import style_formatting

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def is_dict(item):
    return isinstance(item, dict)


def get_diffs(dict1, dict2):
    result_diffs = OrderedDict()
    all_keys = set(dict1.keys() | set(dict2.keys()))

    for key in sorted(all_keys):

        # Untouched items
        if all((key in dict1,
                key in dict2,
                dict1.get(key) == dict2.get(key))):

            result_diffs[key] = {'entry_type': 'stay',
                                 'value': dict1[key]
                                 }
        # Deleted items
        elif key not in dict2:
            result_diffs[key] = {'entry_type': 'delete',
                                 'value': dict1[key]
                                 }
        # Added items
        elif key not in dict1:
            result_diffs[key] = {'entry_type': 'add',
                                 'value': dict2[key]
                                 }
        # Nested items with same keys
        elif is_dict(dict1[key]) and is_dict(dict2[key]):
            children = get_diffs(dict1.get(key), dict2.get(key))
            result_diffs[key] = {'entry_type': 'nested',
                                 'children': children
                                 }
        # After all conditions expecting changed items only
        else:
            result_diffs[key] = {'entry_type': 'change',
                                 'old_value': dict1.get(key),
                                 'new_value': dict2.get(key)
                                 }

    return result_diffs


def generate_diff(file1, file2, style=STYLISH):
    # Loading files to dictionaries
    dict_old = parsing_file(file1)
    dict_new = parsing_file(file2)

    diffs = get_diffs(dict_old, dict_new)

    # Formatting and returning diffs
    return style_formatting(diffs, style)
