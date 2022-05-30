## Reading the annotations file
import json
  
# Opening JSON file
f = open('./annotation/annotations.json')
data = json.load(f)

for asset in data:
    results = [annot['result'] for annot in asset['annotations']]
    obj = {
        'filename': asset['file_upload'].split('-')[1].split('.')[0],
        'file': asset['file_upload'].split('-')[1],
        'annotations': results
    }

    json_object = json.dumps(obj, indent=4)
 
    file = open(f"./annotation/json/{obj['filename']}.json", 'w')
    with file as f:
        f.write(json_object)