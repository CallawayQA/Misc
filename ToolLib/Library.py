
from bs4 import BeautifulSoup
import requests


def listLink(url):

    #url = 'https://www.jackwolfskin.com'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urlList = []

    for link in soup.findAll('a'):
        #print(link.get('href'))
        urlList.append(link.get('href'))

    return urlList

def checkURL(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Working"
        else:
            return "Not Working"
    except:
        return "Error"


def test():
    for i in range (18):
        print(i)


def wrtText(fileName, value1, value2):

    with open(fileName, 'a') as f:
        f.write(value1)
        f.write('----->')
        f.write(value2)
        f.write('\n')

