import requests

def generate_movie(prompt):
    response = requests.post("https://api.runwayml.com/v1/projects", json={"prompt": prompt})
    print(response.json())

generate_movie("Create an AI movie scene with futuristic cars")
