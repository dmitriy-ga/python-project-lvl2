from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.json import json_format


def style_formatting(item, style):
    match style:
        case 'stylish':
            return stylish_format(item)
        case 'plain':
            return plain_format(item)
        case 'json':
            return json_format(item)
