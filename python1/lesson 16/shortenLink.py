import requests

def shorten_link(link, name):
    API_KEY = "62005ceb66a7c4198d32018aba5391d7"
    BASE_URL = "https://cutt.ly/api/api.php"

    #VARIABLE
    payload = {"key" : API_KEY, "short" : link, "name" : name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    try:
        title = data['url']['title']
        shorten_link = data['url']['shortLink']
        status = data['url']['status']
        print(f"Title   : {title}")
        print(f"Link    : {shorten_link}")
        print(f"status  : {status}")

    except:
        status = data['url']['status']
        print(f"Error status : {status}")

    print("try to manage data")

link = input("Insert the link       : ")
name = input("give the link name    : ")
shorten_link(link, name)