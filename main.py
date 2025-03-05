# main.py
import requests

def get_website_content(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    print(get_website_content('https://www.example.com'))
