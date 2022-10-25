from collections import OrderedDict
from gendiff.input_reader import parse_file
from gendiff.formatters.output_formatters import style_formatting, STYLISH

STAY = 'stay'
DELETE = 'delete'
ADD = 'add'
NESTED = 'nested'
CHANGE = 'change'


def get_diffs(dictionary1, dictionary2):
    result_diffs = OrderedDict()
    all_keys = set(dictionary1.keys() | set(dictionary2.keys()))

    for key in sorted(all_keys):

        # Untouched items
        if all((key in dictionary1,
                key in dictionary2,
                dictionary1.get(key) == dictionary2.get(key))):

            result_diffs[key] = {'entry_type': STAY,
                                 'value': dictionary1[key]
                                 }
        # Deleted items
        elif key not in dictionary2:
            result_diffs[key] = {'entry_type': DELETE,
                                 'value': dictionary1[key]
                                 }
        # Added items
        elif key not in dictionary1:
            result_diffs[key] = {'entry_type': ADD,
                                 'value': dictionary2[key]
                                 }
        # Nested items with same keys
        elif all((isinstance(dictionary1[key], dict),
                  isinstance(dictionary2[key], dict)
                  )):

            children = get_diffs(dictionary1.get(key),
                                 dictionary2.get(key))
            result_diffs[key] = {'entry_type': NESTED,
                                 'children': children
                                 }
        # After all conditions expecting changed items only
        else:
            result_diffs[key] = {'entry_type': CHANGE,
                                 'old_value': dictionary1.get(key),
                                 'new_value': dictionary2.get(key)
                                 }

    return result_diffs


def generate_diff(file1, file2, style=STYLISH):
    # Loading files to dictionaries
    first_dictionary = parse_file(file1)
    second_dictionary = parse_file(file2)

    generated_diffs = get_diffs(first_dictionary, second_dictionary)

    # Formatting and returning diffs
    return style_formatting(generated_diffs, style)
