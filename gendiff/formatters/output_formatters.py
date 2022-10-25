from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.json import json_format

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def style_formatting(item, style):
    if style == STYLISH:
        return stylish_format(item)

    elif style == PLAIN:
        return plain_format(item)

    elif style == JSON:
        return json_format(item)

    else:
        raise ValueError('Style format not found')
