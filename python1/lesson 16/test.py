import requests


def shorten_link(link, name):
    API_KEY = 'efe919e3ed61778fc34e57b11e7fff683ecaf'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': link, 'name': name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print(f'Title : {title}')
        print(f'link : {short_link}')

    except:
        status = data['url']['status']
        print(f'Error status {status}')

link = input("Insert the link : ")
name = input("Give the link name : ")

shorten_link(link,name)