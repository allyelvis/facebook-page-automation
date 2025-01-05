import requests

PAGE_ACCESS_TOKEN = 'your_long_lived_page_access_token'

def add_cta_button(button_text, link):
    page_id = 'your_page_id'
    url = f'https://graph.facebook.com/v18.0/{page_id}/call_to_actions'
    payload = {
        'type': 'BOOK_NOW',
        'access_token': PAGE_ACCESS_TOKEN,
        'title': button_text,
        'url': link
    }
    response = requests.post(url, data=payload)
    print(response.json())

add_cta_button("Generate Now", "https://generatorhub.com")
