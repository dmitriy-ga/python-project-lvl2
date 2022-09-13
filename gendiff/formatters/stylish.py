import json
from collections import OrderedDict


def apply_stylish_symbols(diff_dict):
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
                    apply_stylish_symbols(diff_dict[key]['children'])

    return formatted_dict


def stylish_format(diffs):
    styled_dict = json.dumps(apply_stylish_symbols(diffs),
                             indent=4, separators=('', ': '))

    styled_dict = styled_dict.replace('"', '')
    return styled_dict
