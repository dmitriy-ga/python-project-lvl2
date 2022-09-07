import json
from collections import OrderedDict


def stylish(item):
    def stylish_format(diff_dict):
        formatted_dict = OrderedDict()

        for key, value in diff_dict.items():
            match value['action']:
                case 'add':
                    formatted_dict[f'+ {key}'] = diff_dict[key]['value']
                case 'delete':
                    formatted_dict[f'- {key}'] = diff_dict[key]['value']
                case 'stay':
                    formatted_dict[f'  {key}'] = diff_dict[key]['value']
                case 'change':
                    formatted_dict[f'- {key}'] = diff_dict[key]['old_value']
                    formatted_dict[f'+ {key}'] = diff_dict[key]['new_value']
                case 'nested':
                    formatted_dict[f'  {key}'] = \
                        stylish_format(diff_dict[key]['value'])
        return formatted_dict

    styled_dict = json.dumps(stylish_format(item),
                             indent=4, separators=('', ': '))
    styled_dict = styled_dict.replace('"', '')
    print(styled_dict)
    return styled_dict


def plain(diffs, working_directory=''):

    def convert_item_to_plain(item):
        match item:
            case None:
                return 'null'
            case bool() | int():
                return str(item).lower()
            case str():
                return f"'{item}'"
            case dict():
                return '[complex value]'

    result = []

    for key, value in diffs.items():
        path = f'{working_directory}.{key}' if working_directory else key
        match value['action']:

            case 'add':
                added_value = convert_item_to_plain(diffs[key]["value"])
                result.append(
                    f"Property '{path}' was added with value: {added_value}")

            case 'delete':
                result.append(f"Property '{path}' was removed")

            case 'change':
                old_value = convert_item_to_plain(diffs[key]['old_value'])
                new_value = convert_item_to_plain(diffs[key]['new_value'])
                result.append(f"Property '{path}' was updated. "
                              f"From {old_value} to {new_value}")

            case 'nested':
                result.append(plain(diffs[key]['value'], path))

    return '\n'.join(result)


def style_formatting(item, style='stylish'):
    match style:
        case 'stylish':
            return stylish(item)
        case 'plain':
            return plain(item)
