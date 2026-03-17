import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"
    headers = {
        "x-api-key": "live_a13rV4ISjre8L3Ol731HsVQ3EFKzyfe5vbjKZ8O1sulsRIZiMsjXaNPv4FZo4MXS"
    }

    resposta = requests.get(url, headers=headers)


    return resposta.json()

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)

    return resposta.json()[0]