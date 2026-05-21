import requests
import pandas as pd

# exploring api keys before using 

# TODO. get api key from .env

def main():
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'from=2026-05&'
       'sortBy=popularity&'
       'apiKey=#INSERT_API_KEY_HERE')
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    print(len(response.json()))
    print(type(response.json()))
    print(pd.DataFrame(response.json()['articles']["content"]))


if __name__ == "__main__":
    main()