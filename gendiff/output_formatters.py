import json
from collections import OrderedDict


def stylish(item):
    formatted_dict = OrderedDict()

    for key, value in item.items():
        match value['action']:
            case 'add':
                formatted_dict[f'+ {key}'] = item[key]['value']
            case 'delete':
                formatted_dict[f'- {key}'] = item[key]['value']
            case 'stay':
                formatted_dict[f'  {key}'] = item[key]['value']
            case 'change':
                formatted_dict[f'- {key}'] = item[key]['old_value']
                formatted_dict[f'+ {key}'] = item[key]['new_value']

    styled_dict = json.dumps(formatted_dict, indent=4, separators=('', ': '))
    styled_dict = styled_dict.replace('"', '')
    print(styled_dict)
    return styled_dict


def style_formatting(item, style='stylish'):
    match style:
        case 'stylish':
            return stylish(item)
