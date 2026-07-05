import os
import csv
import json

INPUT_FILE="raw_data.csv"
OUTPUT_FILE="converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print('No csv file found')
        return []
    with open(INPUT_FILE,'r',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        data=list(reader)
        return data

def save_as_json(data,filename):
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=3)
    print(f'Converted {len(data)} records to {filename}')

def preview_data(data,count=4):
    for row in data[:count]:
        print(json.dumps(row,indent=2))
    print('..........')

def main():
    data=load_csv_data(INPUT_FILE)
    if not data:
        return
    save_as_json(data,OUTPUT_FILE)
    preview_data(data)

if __name__=="__main__":
    main()



