import csv
import json
from collections import OrderedDict
columns = ['name', 'age', 'education']
dict = [{'name': 'Ivan', 'age': 26, 'education': 'Engineering'},
        {'name': 'Vladimir', 'age': 36, 'education': 'Philosophy'},
        {'name': 'Anna', 'age': 22, 'education': 'Dentist'},]
with open ('dict.csv','w') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(dict)

def convert_csv_to_json(csv_file_path):
    json_data = []
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            json_data.append(OrderedDict(row))
    return json.dumps(json_data, indent=4)

csv_file_path = 'dict.csv'
json_output = convert_csv_to_json(csv_file_path)
print(json_output)