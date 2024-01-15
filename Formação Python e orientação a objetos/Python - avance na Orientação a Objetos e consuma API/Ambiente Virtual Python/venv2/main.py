from fastapi import FastAPI, Query
import requests

# Object FastAPI()
app = FastAPI()

#decorater
@app.get('/api/hello')
def hello_world():
    '''
    Hello World App
    EndPoint usade to show a Hello World message
    :return: 'Hello' : 'World'
    '''
    return {'Hello' : 'World'}

@app.get('/api/restaurant/')
def get_restaurants(restaurant: str = Query(None)):
    '''
    Endpoint usage to show restaurant menu
    :param restaurant:
    :return: menu
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    # code 200: connected successfully
    if response.status_code == 200:
        json_datas = response.json()
        if restaurant is None:
            return {'Dados' : json_datas}
        restaurant_datas = []
        for item in json_datas:
            if item['Company'] == restaurant:
                restaurant_datas.append({
                    "item"       : item['Item'],
                    "price"      : item['price'],
                    "description": item['description']
                })
        return  {'Restaurant': restaurant,
                 'Menu'      : restaurant_datas}
    else:
        return {'Error' : f'{response.status_code} - {response.text}'}
