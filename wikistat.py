from bs4 import BeautifulSoup
import unittest
import re

def parse(path_to_file):  
    f = open(path_to_file, encoding = 'utf-8')
    html = f.read()
    f.close()
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
        if re.match(r'\b[ETC]', h.text):
            headers +=1
        else: 
            continue 
   
     
    #Поиск максимальноййй последовательности ссылок <a>
      
    linkslen = 0
    #print(maindiv.find_all('a'))
    for a in maindiv.find_all('a'):
       # print('tag: ', a.name)
        count_loc=1
        #print([a.find_next_siblings()])
        for s in  a.find_next_siblings():
             #print(s.name)
            if s.name =='a':
                count_loc +=1
                 #print('count: ', count_loc)
            else:
                
                if linkslen < count_loc:
                    linkslen = count_loc
                    count_loc = 0
                    break
                count_loc = 0
                
         
        if linkslen < count_loc:
            linkslen = count_loc
        #print ('\n', linkslen, '\n')
        
        
    
      
  
   
                    
   
                    
    #Поиск невложенных списков
    lists = 0    
    for l in maindiv.find_all(['ul', 'ol']):
        li_test = True
        for parent in l.parents:
            if parent.name in ['ul', 'ol']:
                li_test = False
                break

        if li_test: lists +=1
      
          
        
    
    #print([imgs, headers, linkslen, lists])
    return [imgs, headers, linkslen, lists]


def build_bridge(path, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""

    # напишите вашу реализацию логики по вычисления кратчайшего пути здесь

def getlinks(page):
    soup = BeautifulSoup(page, 'lxml')
    
    

def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    # получаем список страниц, с которых необходимо собрать статистику 
    pages = build_bridge(path, start_page, end_page)
    # напишите вашу реализацию логики по сбору статистики здесь

    return statistic
    
    


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),
            )

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    parse('wiki/Brain')
    unittest.main()