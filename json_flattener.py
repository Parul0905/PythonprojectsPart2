import json
import os

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

def flatten_json(data,parent_key='',sep='.'):
    items={}
    if isinstance(data,dict):
        for k,v in data.items():
            full_key=f"{parent_key}{sep}{k}" if parent_key else k
            print(full_key)
            items.update(flatten_json(v,full_key,sep=sep))

    elif isinstance(data,list):
        for idx,itm in enumerate(data):
            full_key=f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(itm,full_key,sep=sep))


    else:
        items[parent_key]=data
    return items
def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' does not exist.")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as infile:
        nested_data = json.load(infile)

    flattened_data = flatten_json(nested_data)

    with open(OUTPUT_FILE, 'w') as outfile:
        json.dump(flattened_data, outfile, indent=4)

    print(f"Flattened data has been written to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()