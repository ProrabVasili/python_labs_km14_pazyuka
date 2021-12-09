import json
with open('image_info_test-dev2017.json') as f:
    data = json.load(f)
print(f'Number of photos: {len(data["images"])}')
print(f'\nNumber of unique category names: {len(set([i["name"] for i in data["categories"]]))}')
dva = [[i['coco_url'], i['height'], i['width'], i['id']] for i in data['images'] if i['file_name'] == '000000000001.jpg']
nam = ['\nCoco url','Height','Width','ID']
[print(f'{nam[i]}: {dva[0][i]}') for i in range(len(nam))]
r = [i for i in data['images']]
t = max([i['id'] for i in r])
print(f'\nFile name with max ID: {"".join([i["file_name"] for i in r if i["id"] == t])}')
