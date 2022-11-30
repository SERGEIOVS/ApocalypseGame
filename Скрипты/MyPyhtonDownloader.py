import requests

name = '123'

def save_file_from_www(link):
    filename = link.split('/')[-1]

    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)


run = True

while run:

        link = input('link : ')
        save_file_from_www(link)
