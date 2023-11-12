import json
List = [{ "score": 0.0009456152645028281,"weight": 1},
        { "score": 0.0230589189375815523,"weight": 0.3456},
        { "score": 0.2358374937294729421,"weight": 0.8923},
        { "score": 0.9846776542353754874,"weight": 0.8274},
        { "score": 0.8921390834578902345,"weight": 1.3452},]
with open ("List.json","w") as  json_file:
    json.dump(List,json_file)
def calculate_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        product_sum = sum(item['score'] * item['weight'] for item in data)
        return round(product_sum, 3)

file_path = "List.json"
result = calculate_json(file_path)
print(result)