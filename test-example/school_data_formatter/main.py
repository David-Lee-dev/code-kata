CODE = 3
NAME = 4
OLD_ADDRESS_TOKEN_1 = 14
OLD_ADDRESS_TOKEN_2 = 15
ADDRESS_CODE = 16
NEW_ADDRESS_TOKEN_1 = 18
NEW_ADDRESS_TOKEN_2 = 19

import json

with open('middle.json', 'r') as f:
    middle = json.load(f)
with open('high.json', 'r') as f:
    high = json.load(f)
with open('special.json', 'r') as f:
    special = json.load(f)
with open('etc.json', 'r') as f:
    etc = json.load(f)

data = high['body'] + special['body'] + etc['body']


def add_to_tree(tree, word, flag):
    current_node = tree
    for i, char in enumerate(word):
        if char not in current_node:
            current_node[char] = {'children': {}, 'end': False}
        current_node = current_node[char]['children']
    current_node['end'] = flag


def build_tree(schools):
    tree = {}
    for school in schools:
        name = school[NAME]
        flag = '학교'
        if '중고등학교' in name:
            name = list(name[:-5])
            flag = '중고등학교'
        elif name.endswith('(중)'):
            name = list(name[:-5])
            flag = '학교(중)'
        elif name.endswith('(초)'):
            name = list(name[:-5])
            flag = '학교(초)'
        elif name.endswith('(고)'):
            name = list(name[:-5])
            flag = '학교(고)'
        elif '중학교' in name:
            name = list(name[:-3])
            flag = '중학교'
        elif '고등학교' in name:
            name = list(name[:-4])
            flag = '고등학교'
        else:
            name = list(name[:-2])
            flag = '학교'

        add_to_tree(tree, name, flag)
    return tree


def traverse_and_combine_keys(data, prefix=''):
    result = []
    for key, value in data.items():
        if key == "end" and value is not False:
            result.append(prefix + data['end'])
        elif key != "end":
            combined_key = prefix + key
            children = value.get('children', {})
            result.extend(traverse_and_combine_keys(children, combined_key))
    return result


def make_school_map(schools):
    result = {}

    for school in schools:
        name = school[NAME]
        code = school[CODE]
        address_code = school[ADDRESS_CODE]
        old_address = school[OLD_ADDRESS_TOKEN_1] + ' ' + school[OLD_ADDRESS_TOKEN_2]
        new_address = school[NEW_ADDRESS_TOKEN_1] + ' ' + school[NEW_ADDRESS_TOKEN_2]

        if result.get(name):
            result[name + '_2'] = {
                'schoolCode': code,
                'addressCode': address_code,
                'oldAddress': old_address,
                'newAddress': new_address,
                'schoolName': name
            }
        else:
            result[name] = {
                'schoolCode': code,
                'addressCode': address_code,
                'oldAddress': old_address,
                'newAddress': new_address,
                'schoolName': name
            }

    return result


name_map = build_tree(data)
school_map = make_school_map(data)

with open('school_name_search_map.json', 'w', encoding='utf-8') as f:
    json.dump({k.encode('utf-8').decode('utf-8'): v for k, v in name_map.items()}, f, ensure_ascii=False)

with open('school_info_map.json', 'w', encoding='utf-8') as f:
    json.dump({k.encode('utf-8').decode('utf-8'): v for k, v in school_map.items()}, f, ensure_ascii=False)
