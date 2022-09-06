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


def style_formatting(item, style='stylish'):
    match style:
        case 'stylish':
            return stylish(item)
