import requests

PAGE_ACCESS_TOKEN = 'your_long_lived_page_access_token'

def create_facebook_page(page_name, page_category):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    payload = {
        'access_token': PAGE_ACCESS_TOKEN,
        'name': page_name,
        'category': page_category,
        'about': 'Generate Apps, Music, and Movies easily!',
    }
    response = requests.post(url, data=payload)
    print(response.json())

create_facebook_page("Generator Hub", "Software Company")
