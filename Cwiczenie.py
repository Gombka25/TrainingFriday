# 3 adrest url, bedzie iterowal po nich, wysle geta do nich zeby zczytac tresc strony i zloczy wystapienia jakichs slow
import requests

URLs = ['http://www.interia.pl', 'http://www.onet.pl', 'http://www.wp.com']

def count_words_on_website(url, word):
    counter = 0
    response = requests.get(url=url,verify=False)
    html = response.text
    print(html.count(word))

count_words_on_website('http://www.onet.pl', "onet")
