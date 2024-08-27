"""
import requests
from bs4 import BeautifulSoup

def categorize_words_from_url(url, categories):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    if text:
        words = text.split(" ")
        if words:
            return words[0]
    return None

url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/abbamarad-1C009/"
categories = ["noun", "verb", "adjective"]
result = categorize_words_from_url(url, categories)
if result:
    print("The first word from the text is:", result)
else:
    print("No text found at the URL.")
"""
"""
import requests
from bs4 import BeautifulSoup

def categorize_words_from_url(url, categories):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    word_categories = []
    if text:
        words = text.split(" ")
        if words:
            first_word = words[0]
            for category in categories:
                if category in text:
                    word_categories.append((first_word, category))
    return word_categories

url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/abbamarad-1C009/"
categories = ["ige", "főnév"]
result = categorize_words_from_url(url, categories)
if result:
    print("The word-category pairs from the text are:", result)
else:
    print("No text found at the URL.")
"""

"""
import requests
from bs4 import BeautifulSoup

def categorize_words_from_url(url, categories):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text().replace("\n", "")
    word_categories = []
    if text:
        words = text.split(" ")
        if words:
            first_word = words[0]
            for category in categories:
                if category in text:
                    word_categories.append((first_word, category))
    return word_categories

url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/abbamarad-1C009/"
categories = ["tárgyatlan ige", "főnév"]
result = categorize_words_from_url(url, categories)
if result:
    print(result)
else:
    print("No text found at the URL.")
"""
"""
import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {'class': 'list-group mb-3'})
    links = [a['href'] for a in div.find_all('a', href=True)]
    return links

url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/"
result = extract_links(url)

links = extract_links(url)
urls = []
for link in links:
    urls.append("https://www.arcanum.com/" + link)

if result:
    print(result)
else:
    print("No links found.")

def categorize_words_from_urls(urls, categories):
    word_categories = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().replace("\n", "")
        if text:
            words = text.split(" ")
            if words:
                first_word = words[0]
                for category in categories:
                    if category in text:
                        word_categories.append((first_word, category))
    return word_categories
    
categories = ["tárgyatlan ige", "főnév",]
result = categorize_words_from_urls(urls, categories)
if result:
    print(result)
else:
    print("No text found at the URLs.")
"""

"""
import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {'class': 'list-group mb-3'})
    links = [a['href'] for a in div.find_all('a', href=True)]
    return links

url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/"
result = extract_links(url)

links = extract_links(url)
urls = []
for link in links:
    urls.append("https://www.arcanum.com/" + link)

def categorize_words_from_urls(urls, categories):
    word_categories = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().replace("\n", "")
        if text:
            words = text.split(" ")
            if words:
                first_word = words[0]
                for category in categories:
                    if category in text:
                        word_categories.append((first_word, category))
    return word_categories
    
categories = ["tárgyatlan ige", "főnév",]
result = categorize_words_from_urls(urls, categories)
if result:
    for word_category in result:
        print(word_category)
else:
    print("No text found at the URLs.")
"""
"""
import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {'class': 'list-group mb-3'})
    links = [a['href'] for a in div.find_all('a', href=True)]
    return links

i = 2
while i <= 32:
    url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/?page=" + str(i)
    result = extract_links(url)
    links = extract_links(url)
    urls = []
    for link in links:
        urls.append("https://www.arcanum.com/" + link)

    def categorize_words_from_urls(urls, categories):
        word_categories = []
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().replace("\n", "")
            if text:
                words = text.split(" ")
                if words:
                    first_word = words[0]
                    for category in categories:
                        if category in text:
                            word_categories.append((first_word, category))
        return word_categories

    categories = ["tárgyatlan ige", "főnév",]
    result = categorize_words_from_urls(urls, categories)
    if result:
        for word_category in result:
            print(word_category)
    else:
        print("No text found at the URLs.")
    i += 1
"""
"""
import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {'class': 'list-group mb-3'})
    links = [a['href'] for a in div.find_all('a', href=True)]
    return links

def categorize_words_from_urls(urls):
    word_categories = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'class':'Lexikonok_FE_C_msz___rtelmez_'})
        if div:
            category = div.find('span', {'class': 'Lexikonok_FE_Cmsz'}).text.strip()
            first_word = div.find('span', {'class': 'Lexikonok_FE_C_msz__rtelmez'}).text.strip()
            word_categories.append((first_word, category))
    return word_categories


i = 2
while i <= 32:
    url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/?page=" + str(i)
    links = extract_links(url)
    urls = []
    for link in links:
        urls.append("https://www.arcanum.com/" + link)

    result = categorize_words_from_urls(urls)
    if result:
        for word_category in result:
            print(word_category)
    else:
        print("No text found at the URLs.")
    i += 1
"""

import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {'class': 'list-group mb-3'})
    links = [a['href'] for a in div.find_all('a', href=True)]
    return links

i = 2
while i <= 32:
    url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/?page=" + str(i)
    result = extract_links(url)
    links = extract_links(url)
    urls = []
    for link in links:
        urls.append("https://www.arcanum.com/" + link)

    def categorize_words_from_urls(urls):
        word_categories = []
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            div = soup.find('div', {'class': 'Lexikonok_FE_C_msz___rtelmez_'})
            if div:
                first_word = div.find('span', {'class': 'Lexikonok_FE_C_msz___rtelmez_'}).text.strip()
                category = div.find('span', {'class': 'Lexikonok_FE_C_msz___'}).text.strip()
                word_categories.append((first_word, category))
        return word_categories

    result = categorize_words_from_urls(urls)
    if result:
        for word_category in result:
            print(word_category)
    else:
        print("No text found at the URLs.")
    i += 1


