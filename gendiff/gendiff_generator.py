from collections import OrderedDict
import json


def generate_diff(file1, file2):
    # Loading files to dictionaries
    dict1 = json.load(open(file1))
    dict2 = json.load(open(file2))

    # Dictionary of untouched items
    stays_wo_syms = dict(dict1.items() & dict2.items())
    stays = {}
    for i in stays_wo_syms.keys():
        new_name = '  ' + i
        stays[new_name] = stays_wo_syms[i]
    del stays_wo_syms

    # Dictionary of deleted items
    deletes_wo_syms = dict(dict1.items() - dict2.items())
    deletes = {}
    for i in deletes_wo_syms.keys():
        new_name = '- ' + i
        deletes[new_name] = deletes_wo_syms[i]
    del deletes_wo_syms
    # print(deletes)

    # Dictionary of added items
    adds_wo_syms = dict(dict2.items() - dict1.items())
    adds = {}
    for i in adds_wo_syms.keys():
        new_name = '+ ' + i
        adds[new_name] = adds_wo_syms[i]
    del adds_wo_syms
    # print(adds)

    # Python dictionary with diffs
    diffs = OrderedDict(stays | deletes | adds)
    for name in sorted(diffs, key=lambda x: x.split()[-1]):
        diffs.move_to_end(name)
    # print(diffs)

    new_json = json.dumps(diffs, indent=2)
    new_json = new_json.replace("\"", "")
    print(new_json)
