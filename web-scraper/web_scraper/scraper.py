""" install this (pip3 install requests Collecting requests) so you can import requests
 upgrade pip if you still have issues using this command "pip3 install --upgrade pip or better to 
 use this command => poetry add requests beautifulsoup4 """ 

import json
import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    count=BeautifulSoup(requests.get(url).content, "html.parser").find_all(text="citation needed")
    return len(count)

def get_citations_needed_report(url):
    content = []
    count=BeautifulSoup(requests.get(url).content,  "html.parser").find_all("p")
    for p in count:
        citations_needed=p.find_all('a',title='Wikipedia:Citation needed')
        for citation in citations_needed:
            content.append(p.text)

    return((content))


if __name__ == "__main__":
    url="https://en.wikipedia.org/wiki/History_of_Mexico"
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
    