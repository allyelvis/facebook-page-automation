import requests

PAGE_ACCESS_TOKEN = 'your_long_lived_page_access_token'

def create_post(message, link):
    page_id = 'your_page_id'
    url = f'https://graph.facebook.com/v18.0/{page_id}/feed'
    payload = {
        'message': message,
        'link': link,
        'access_token': PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    print(response.json())

create_post("Try our new App Generator!", "https://appgenerator.com")
