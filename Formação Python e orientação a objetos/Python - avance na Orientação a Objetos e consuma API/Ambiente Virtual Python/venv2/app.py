import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
# url = 'https://guilhermeonrails.github.io/api-restaurantes/taurantes.json' # Error URL

response = requests.get(url)
print(response)

# code 200: connected successfully
if response.status_code == 200:
    json_datas = response.json()
    restaurant_datas = {}

    for item in json_datas:
        restaurant_name = item['Company']

        if restaurant_name not in restaurant_datas:
            restaurant_datas[restaurant_name] = []

        restaurant_datas[restaurant_name].append({
            "item"       : item['Item'],
            "price"      : item['price'],
            "description": item['description']
        })
else:
    print(f'Error: {response}')

# print(restaurant_datas['McDonald’s'])

for r_name, r_data in restaurant_datas.items():
    name_file = f'{r_name}.json'
    try:
        with open(name_file, 'w') as restaurant_file:
            json.dump(r_data, restaurant_file, indent=4)
    except:
        print("@ WARNING:")
        print("\tCannot create the file!")
        print("\tThe application can be run. And it will close!")
        exit(0)

