import requests

def get_products():
    try:
        # comment: 
         response = requests.get('https://dummyjson.com/products')
         print(response)
         print(response.json())
    except Exception as e:
        raise e
   
get_products()