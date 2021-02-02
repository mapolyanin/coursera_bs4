from bs4 import BeautifulSoup
import unittest
import re

def parse(path_to_file):  
    html = open(path_to_file, encoding = 'utf-8').read()
    soup = BeautifulSoup(html, 'lxml')
    
    maindiv = soup.find('div', id= 'bodyContent')
    
    #Поиск изображений
    imgs = 0
    for i in maindiv.find_all('img'):
        #print (type(i['width']))
        try:
            if int(i['width']) >= 200: 
                imgs +=1
            
        except:
            continue
    
    #Поиск заголовков
    headers = 0
    for h in maindiv.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        #print(h.text)
        if re.search(r'[ETC]', h.text):
            headers +=1
        else: 
            continue 
        
    
    
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибкой UnicodeDecodeError
    #imgs = None
    #headers = None
    linkslen = None
    lists = None
    
    print([imgs, headers, linkslen, lists])
    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    parse('wiki/Stone_Age')
    #unittest.main()